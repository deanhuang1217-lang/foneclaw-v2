#!/usr/bin/env python3
"""Rebuild _build_cache.pkl from original images on disk."""
import pickle, base64, os, glob

base = os.path.dirname(os.path.abspath(__file__))
cache_path = os.path.join(base, '_build_cache.pkl')

# Load existing cache to get the structure
old_cache = pickle.load(open(cache_path, 'rb'))
old_imgs = old_cache['imgs']

# Map of cache keys to file paths
img_map = {
    'hero_banner': 'images/hero_banner.jpg',
    'features_banner': 'images/features_banner.jpg',
    'feat_voice': 'images/feat_voice.jpg',
    'feat_agent': 'images/feat_agent.jpg',
    'feat_system': 'images/feat_system.jpg',
    'feat_ui': 'images/feat_ui.jpg',
    'feat_driving': 'images/feat_driving.jpg',
    'feat_multistep': 'images/feat_multistep.jpg',
    'feat_elderly': 'images/feat_elderly.jpg',
    'feat_remote': 'images/feat_remote.jpg',
    'feat_apps': 'images/feat_apps.jpg',
    'feat_memory': 'images/feat_memory.jpg',
    'feat_privacy': 'images/feat_privacy.jpg',
}

# Find article images
for f in glob.glob(os.path.join(base, 'images/articles/*.jpg')):
    key = os.path.splitext(os.path.basename(f))[0]
    img_map[f'articles/{key}'] = f'images/articles/{key}.jpg'

# Rebuild cache
new_imgs = {}
loaded = 0
skipped = 0
for key, rel_path in img_map.items():
    abs_path = os.path.join(base, rel_path)
    if os.path.exists(abs_path):
        with open(abs_path, 'rb') as f:
            img_bytes = f.read()
        new_imgs[key] = base64.b64encode(img_bytes).decode()
        loaded += 1
        print(f"  ✅ {key}: {len(img_bytes)//1024}KB")
    elif key in old_imgs:
        new_imgs[key] = old_imgs[key]
        skipped += 1
        print(f"  ⏭️ {key}: using cached version")
    else:
        print(f"  ❌ {key}: NOT FOUND")

# Keep any keys from old cache that we didn't map
for key in old_imgs:
    if key not in new_imgs:
        new_imgs[key] = old_imgs[key]
        print(f"  ⏭️ {key}: kept from old cache")

# Load favicon (use small 16x16 version for base64 embedding)
favicon_path = os.path.join(base, 'favicon_small.png')
if os.path.exists(favicon_path):
    with open(favicon_path, 'rb') as f:
        icon_b64 = base64.b64encode(f.read()).decode()
    print(f"  ✅ favicon_small.png: {len(icon_b64)} chars base64")
else:
    icon_b64 = old_cache.get('icon_b64', '')
    print(f"  ⏭️ favicon: using cached version")

new_cache = {
    'imgs': new_imgs,
    'icon_b64': icon_b64
}

pickle.dump(new_cache, open(cache_path, 'wb'))
print(f"\n✅ Cache rebuilt: {loaded} loaded from disk, {skipped} from old cache")
print(f"Total images: {len(new_imgs)}")
