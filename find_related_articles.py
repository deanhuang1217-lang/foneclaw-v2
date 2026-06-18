#!/usr/bin/env python3
"""Find related articles and their keywords for internal linking planning."""
import sys
sys.path.insert(0, '/home/administrator/clawfone-v2')

from article_keywords_data import ARTICLE_KEYWORDS

def find_related_articles(topic, top_n=5):
    """Find articles related to a topic based on keyword overlap.
    
    Args:
        topic: description of the new article topic
        top_n: number of related articles to return
    
    Returns:
        list of (slug, keywords, relevance_score) tuples
    """
    topic_words = set(topic.lower().split())
    
    scored = []
    for slug, keywords in ARTICLE_KEYWORDS.items():
        # Calculate relevance based on keyword overlap
        score = 0
        for kw in keywords:
            kw_words = set(kw.lower().split())
            overlap = len(topic_words & kw_words)
            score += overlap
        
        if score > 0:
            scored.append((slug, keywords, score))
    
    # Sort by relevance score
    scored.sort(key=lambda x: x[2], reverse=True)
    return scored[:top_n]

def get_keywords_for_articles(slugs):
    """Get keywords for specific articles.
    
    Args:
        slugs: list of article slugs
    
    Returns:
        dict of slug -> [keywords]
    """
    result = {}
    for slug in slugs:
        if slug in ARTICLE_KEYWORDS:
            result[slug] = ARTICLE_KEYWORDS[slug]
    return result

def suggest_keywords_for_article(topic, existing_slugs=None):
    """Suggest keywords to include in a new article for natural internal linking.
    
    Args:
        topic: description of the new article topic
        existing_slugs: list of article slugs to link to (optional)
    
    Returns:
        dict with 'related_articles' and 'suggested_keywords'
    """
    if existing_slugs:
        related = [(slug, ARTICLE_KEYWORDS.get(slug, []), 0) for slug in existing_slugs]
    else:
        related = find_related_articles(topic)
    
    suggested = []
    for slug, keywords, score in related:
        for kw in keywords:
            suggested.append({
                'keyword': kw,
                'target_article': slug,
                'target_url': f'/{slug}.html',
            })
    
    return {
        'related_articles': [(slug, keywords) for slug, keywords, _ in related],
        'suggested_keywords': suggested,
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 find_related_articles.py <topic description>")
        print("Example: python3 find_related_articles.py 'voice control cooking kitchen'")
        sys.exit(1)
    
    topic = ' '.join(sys.argv[1:])
    result = suggest_keywords_for_article(topic)
    
    print(f"\n=== Related Articles for: '{topic}' ===\n")
    for slug, keywords in result['related_articles']:
        print(f"  {slug}:")
        print(f"    Keywords: {', '.join(keywords)}")
    
    print(f"\n=== Suggested Keywords to Include ===\n")
    for item in result['suggested_keywords']:
        print(f'  "{item["keyword"]}" -> {item["target_article"]}')
