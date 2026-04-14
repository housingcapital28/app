import requests
import os

# 7 images for prop-dlf1
image_urls = [
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/umatqf36_WhatsApp%20Image%202026-04-14%20at%201.27.15%20PM%20%282%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/euf1eh18_WhatsApp%20Image%202026-04-14%20at%201.27.15%20PM%20%283%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/d1a1rey2_WhatsApp%20Image%202026-04-14%20at%201.27.35%20PM%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/pl73p7rh_WhatsApp%20Image%202026-04-14%20at%201.27.35%20PM%20%282%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/1uxyjaqr_WhatsApp%20Image%202026-04-14%20at%201.27.35%20PM.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/ysys9y9l_WhatsApp%20Image%202026-04-14%20at%201.27.36%20PM%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/6cnul01r_WhatsApp%20Image%202026-04-14%20at%201.27.36%20PM%20%282%29.jpeg"
]

output_dir = "/app/frontend/public/images/properties/prop-dlf1"

for idx, url in enumerate(image_urls, 1):
    try:
        print(f"Downloading image {idx}/7...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        output_path = f"{output_dir}/gallery-{idx}.jpg"
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Saved: /images/properties/prop-dlf1/gallery-{idx}.jpg")
        
    except Exception as e:
        print(f"✗ Error processing image {idx}: {e}")

print(f"\n✅ Successfully downloaded 7 images for prop-dlf1")
