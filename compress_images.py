#!/usr/bin/env python3
"""Auto-compress all images in build cache. Run before or as part of build_multi.py."""
import pickle, base64, io, sys
from PIL import Image

def compress_cache_images(cache_path='_build_cache.pkl', 
                          max_width=99999, max_height=99999, 
                          quality=100, format='JPEG'):
    """Compress all images in cache. Returns (total_before, total_after, count)."""
    cache = pickle.load(open(cache_path, 'rb'))
    total_before = 0
    total_after = 0
    count = 0
    
    for key, img_b64 in cache['imgs'].items():
        img_bytes = base64.b64decode(img_b64)
        original_size = len(img_bytes)
        total_before += original_size
        
        # Skip if already small (< 30KB)
        if original_size < 30 * 1024:
            total_after += original_size
            continue
        
        # Skip favicon/icon (small square images)
        img = Image.open(io.BytesIO(img_bytes))
        w, h = img.size
        if w == h and w <= 200:  # favicon/icon
            total_after += original_size
            continue
        
        # Resize maintaining aspect ratio
        ratio = min(max_width / w, max_height / h)
        if ratio < 1:
            new_w = int(w * ratio)
            new_h = int(h * ratio)
            img = img.resize((new_w, new_h), Image.LANCZOS)
        
        # Compress
        buf = io.BytesIO()
        img.save(buf, format=format, quality=quality, optimize=True)
        compressed = buf.getvalue()
        
        cache['imgs'][key] = base64.b64encode(compressed).decode()
        total_after += len(compressed)
        count += 1
        
        reduction = (1 - len(compressed) / original_size) * 100
        if reduction > 10:  # Only report significant compressions
            print(f"  {key}: {original_size//1024}KB → {len(compressed)//1024}KB ({reduction:.0f}% reduction)")
    
    pickle.dump(cache, open(cache_path, 'wb'))
    return total_before, total_after, count

if __name__ == '__main__':
    print("Compressing images in build cache...")
    before, after, count = compress_cache_images()
    reduction = (1 - after / before) * 100 if before > 0 else 0
    print(f"\nTotal: {before//1024}KB → {after//1024}KB ({reduction:.0f}% reduction, {count} images compressed)")
