#!/usr/bin/env python3
"""Generate Twitter post images with text overlay."""
import os
from PIL import Image, ImageDraw, ImageFont

# Paths
base = os.path.dirname(os.path.abspath(__file__))
deploy = '/home/administrator/foneclaw-deploy/uploads/2026-05-13_1600/images/articles'
output_dir = os.path.join(base, 'twitter_images')
os.makedirs(output_dir, exist_ok=True)

# Twitter recommended size: 1200x675 (16:9)
WIDTH, HEIGHT = 1200, 675

# Post data: (image_file, headline, subtext, cta)
posts = [
    {
        'image': 'howto_driving_voice.jpg',
        'headline': 'Voice Control While Driving',
        'subtext': '48 states ban texting while driving.\n3,000+ deaths/year from distracted driving.',
        'cta': 'What if your phone understood you?',
        'color': '#00d4ff'
    },
    {
        'image': 'uc_cooking.jpg',
        'headline': 'Hands-Free Cooking',
        'subtext': 'Hands covered in flour.\nPhone buzzing on the counter.',
        'cta': 'Your AI handles it.',
        'color': '#3fb950'
    },
    {
        'image': 'howto_elderly_setup.jpg',
        'headline': 'Smartphone for Seniors',
        'subtext': '50M+ US seniors own smartphones.\nMillions struggle to use them.',
        'cta': 'Just say what you want.',
        'color': '#f0883e'
    },
    {
        'image': 'uc_parenting.jpg',
        'headline': 'Parenting Hands-Free',
        'subtext': 'Baby in one arm.\nPhone ringing in the other room.',
        'cta': 'Three commands. Zero hands.',
        'color': '#bc8cff'
    },
    {
        'image': 'uc_emergency.jpg',
        'headline': 'Emergency Voice Commands',
        'subtext': 'You fall. Phone in your pocket.\nYou can\'t reach it.',
        'cta': '"Call 911. Send location to Dad."',
        'color': '#f85149'
    },
    {
        'image': 'uc_visual_impaired.jpg',
        'headline': '100% Voice Control',
        'subtext': '7M visually impaired Americans\nuse smartphones daily.',
        'cta': 'Every function by voice.',
        'color': '#00d4ff'
    },
    {
        'image': 'howto_multistep.jpg',
        'headline': 'Multi-Step Automation',
        'subtext': '"Book earliest flight NYC→LA."\nOne sentence. Five apps. Zero taps.',
        'cta': 'AI that chains actions.',
        'color': '#3fb950'
    },
    {
        'image': 'uc_commuting.jpg',
        'headline': 'Voice Control on the Go',
        'subtext': '27 min average commute.\nHands on wheel. Eyes on road.',
        'cta': 'Your phone handles the rest.',
        'color': '#f0883e'
    },
    {
        'image': 'howto_privacy.jpg',
        'headline': 'Privacy-First AI',
        'subtext': 'Your assistant sends every word\nto the cloud. Always listening.',
        'cta': 'What if the AI lived on YOUR phone?',
        'color': '#bc8cff'
    },
    {
        'image': 'howto_dirty_hands.jpg',
        'headline': 'Hands-Free When It Matters',
        'subtext': 'Elbow-deep in raw chicken.\nPhone buzzing with urgent message.',
        'cta': '"Reply to Mom: Running late."',
        'color': '#f85149'
    },
]

def get_font(size, bold=False):
    """Get font, fallback to default if not available."""
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
    ]
    for path in font_paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def create_twitter_image(post, index):
    """Create a Twitter-optimized image with text overlay."""
    # Load source image
    src_path = os.path.join(deploy, post['image'])
    if not os.path.exists(src_path):
        print(f"  ❌ {post['image']} not found")
        return
    
    # Open and resize image
    img = Image.open(src_path).convert('RGB')
    img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
    
    # Create dark overlay for text readability
    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Gradient overlay (darker at bottom)
    for y in range(HEIGHT):
        alpha = int(180 * (y / HEIGHT))  # 0 at top, 180 at bottom
        draw.rectangle([(0, y), (WIDTH, y+1)], fill=(0, 0, 0, alpha))
    
    img = Image.alpha_composite(img.convert('RGBA'), overlay)
    draw = ImageDraw.Draw(img)
    
    # Fonts
    headline_font = get_font(48, bold=True)
    subtext_font = get_font(28)
    cta_font = get_font(32, bold=True)
    brand_font = get_font(18)
    
    # Colors
    white = (255, 255, 255, 255)
    accent = tuple(int(post['color'].lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (255,)
    gray = (200, 200, 200, 255)
    
    # Draw headline (centered, middle of image)
    headline_bbox = draw.textbbox((0, 0), post['headline'], font=headline_font)
    headline_w = headline_bbox[2] - headline_bbox[0]
    headline_x = (WIDTH - headline_w) // 2
    headline_y = HEIGHT // 2 - 80
    draw.text((headline_x, headline_y), post['headline'], fill=white, font=headline_font)
    
    # Draw accent line under headline
    line_y = headline_y + 60
    line_w = min(headline_w, 200)
    line_x = (WIDTH - line_w) // 2
    draw.rectangle([(line_x, line_y), (line_x + line_w, line_y + 4)], fill=accent)
    
    # Draw subtext (centered)
    subtext_lines = post['subtext'].split('\n')
    subtext_y = line_y + 20
    for line in subtext_lines:
        subtext_bbox = draw.textbbox((0, 0), line, font=subtext_font)
        subtext_w = subtext_bbox[2] - subtext_bbox[0]
        subtext_x = (WIDTH - subtext_w) // 2
        draw.text((subtext_x, subtext_y), line, fill=gray, font=subtext_font)
        subtext_y += 40
    
    # Draw CTA (centered, accent color)
    cta_bbox = draw.textbbox((0, 0), post['cta'], font=cta_font)
    cta_w = cta_bbox[2] - cta_bbox[0]
    cta_x = (WIDTH - cta_w) // 2
    cta_y = subtext_y + 20
    draw.text((cta_x, cta_y), post['cta'], fill=accent, font=cta_font)
    
    # Draw FoneClaw brand (bottom right)
    brand_text = 'FoneClaw — AI Voice Agent for Android'
    brand_bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    brand_w = brand_bbox[2] - brand_bbox[0]
    draw.text((WIDTH - brand_w - 20, HEIGHT - 35), brand_text, fill=(150, 150, 150, 200), font=brand_font)
    
    # Save
    output_path = os.path.join(output_dir, f'post_{index:02d}.png')
    img.convert('RGB').save(output_path, quality=95)
    size_kb = os.path.getsize(output_path) // 1024
    print(f"  ✅ Post {index}: {output_path} ({size_kb}KB)")

# Generate all images
print("=== 生成Twitter帖子图片 ===")
for i, post in enumerate(posts, 1):
    create_twitter_image(post, i)

print(f"\n✅ 完成，共生成 {len(posts)} 张图片")
print(f"📁 输出目录: {output_dir}")
