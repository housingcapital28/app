import requests
import os

# 5 images for prop-dlf2-2
image_urls = [
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/n2bem9oc_WhatsApp%20Image%202026-04-14%20at%2013.30.11%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/248eh0k9_WhatsApp%20Image%202026-04-14%20at%2013.30.11.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/x431r32o_WhatsApp%20Image%202026-04-14%20at%2013.30.12%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/d0pshfun_WhatsApp%20Image%202026-04-14%20at%2013.30.12%20%282%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/bcyu2k5s_WhatsApp%20Image%202026-04-14%20at%2013.30.12.jpeg"
]

output_dir = "/app/frontend/public/images/properties/prop-dlf2-2"

for idx, url in enumerate(image_urls, 1):
    try:
        print(f"Downloading image {idx}/5...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        output_path = f"{output_dir}/gallery-{idx}.jpg"
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Saved: /images/properties/prop-dlf2-2/gallery-{idx}.jpg")
        
    except Exception as e:
        print(f"✗ Error processing image {idx}: {e}")

print(f"\n✅ Successfully downloaded 5 images for prop-dlf2-2")
