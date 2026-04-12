import requests
from pillow_heif import register_heif_opener
from PIL import Image
import os

# Register HEIF opener with Pillow
register_heif_opener()

# HEIC image URLs provided by user
heic_urls = [
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/cbp6jt8c_IMG_7931.HEIC",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/5vfgclin_IMG_7933.HEIC",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/6ru72tuo_IMG_7934.HEIC",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/u0w6ye7p_IMG_7931%20%281%29.HEIC",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/qfg45000_IMG_7931.HEIC",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/zz8k4ixf_IMG_7933.HEIC",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/15mbpanv_IMG_7936%20%281%29.HEIC",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/wj032169_IMG_7937%20%281%29.HEIC"
]

output_dir = "/app/frontend/public/images/properties/prop-sushant"
os.makedirs(output_dir, exist_ok=True)

converted_paths = []

for idx, url in enumerate(heic_urls, 1):
    try:
        print(f"Downloading image {idx}/{len(heic_urls)}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Save HEIC temporarily
        temp_heic = f"/tmp/temp_{idx}.heic"
        with open(temp_heic, 'wb') as f:
            f.write(response.content)
        
        # Convert to JPG
        print(f"Converting image {idx} to JPG...")
        img = Image.open(temp_heic)
        
        # Convert RGBA to RGB if necessary
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background
        
        # Save as JPG
        output_path = f"{output_dir}/gallery-{idx}.jpg"
        img.save(output_path, 'JPEG', quality=85, optimize=True)
        
        # Store the relative path for frontend
        relative_path = f"/images/properties/prop-sushant/gallery-{idx}.jpg"
        converted_paths.append(relative_path)
        
        print(f"✓ Saved: {relative_path}")
        
        # Clean up temp file
        os.remove(temp_heic)
        
    except Exception as e:
        print(f"✗ Error processing image {idx}: {e}")

print(f"\n✅ Successfully converted {len(converted_paths)} images")
print("\nConverted image paths:")
for path in converted_paths:
    print(f"  {path}")
