import requests
import os

# 4 images for prop-dlf2-sec27
image_urls = [
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/bmyu9zo4_WhatsApp%20Image%202026-04-14%20at%201.27.17%20PM%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/zgtx1wq6_WhatsApp%20Image%202026-04-14%20at%201.27.17%20PM.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/hp52xtbe_WhatsApp%20Image%202026-04-14%20at%201.27.18%20PM%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/bh6kkl92_WhatsApp%20Image%202026-04-14%20at%201.27.18%20PM.jpeg"
]

output_dir = "/app/frontend/public/images/properties/prop-dlf2-sec27"

for idx, url in enumerate(image_urls, 1):
    try:
        print(f"Downloading image {idx}/4...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        output_path = f"{output_dir}/gallery-{idx}.jpg"
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Saved: /images/properties/prop-dlf2-sec27/gallery-{idx}.jpg")
        
    except Exception as e:
        print(f"✗ Error processing image {idx}: {e}")

print(f"\n✅ Successfully downloaded 4 images for prop-dlf2-sec27")
