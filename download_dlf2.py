import requests
import os

# 5 images for prop-dlf2
image_urls = [
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/goistq8l_WhatsApp%20Image%202026-04-14%20at%2013.28.06%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/09u40j79_WhatsApp%20Image%202026-04-14%20at%2013.28.06%20%282%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/63i9ncqg_WhatsApp%20Image%202026-04-14%20at%2013.28.06.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/8i4yy01u_WhatsApp%20Image%202026-04-14%20at%2013.28.07%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/602cdrn1_WhatsApp%20Image%202026-04-14%20at%2013.28.07%20%282%29.jpeg"
]

output_dir = "/app/frontend/public/images/properties/prop-dlf2"

for idx, url in enumerate(image_urls, 1):
    try:
        print(f"Downloading image {idx}/5...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        output_path = f"{output_dir}/gallery-{idx}.jpg"
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Saved: /images/properties/prop-dlf2/gallery-{idx}.jpg")
        
    except Exception as e:
        print(f"✗ Error processing image {idx}: {e}")

print(f"\n✅ Successfully downloaded 5 images for prop-dlf2")
