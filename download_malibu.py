import requests
import os

# 4 images for prop-malibu
image_urls = [
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/3if3oefb_WhatsApp%20Image%202026-04-14%20at%2012.34.45%20PM.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/314cmmsv_WhatsApp%20Image%202026-04-14%20at%2012.53.14%20PM.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/1stfw46j_WhatsApp%20Image%202026-04-14%20at%2012.53.19%20PM.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/5i5kx6lw_WhatsApp%20Image%202026-04-14%20at%2012.53.42%20PM%20%281%29.jpeg"
]

output_dir = "/app/frontend/public/images/properties/prop-malibu"

for idx, url in enumerate(image_urls, 1):
    try:
        print(f"Downloading image {idx}/4...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        output_path = f"{output_dir}/gallery-{idx}.jpg"
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Saved: /images/properties/prop-malibu/gallery-{idx}.jpg")
        
    except Exception as e:
        print(f"✗ Error processing image {idx}: {e}")

print(f"\n✅ Successfully downloaded 4 images for prop-malibu")
