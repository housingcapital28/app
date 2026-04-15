import requests
import os

# 5 additional images for prop-dlf2-2 (batch 2)
image_urls = [
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/9le3hl7i_WhatsApp%20Image%202026-04-14%20at%2013.30.13%20%282%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/rzk2h9q0_WhatsApp%20Image%202026-04-14%20at%2013.30.13.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/87v40c6q_WhatsApp%20Image%202026-04-14%20at%2013.30.14%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/wx9f5k0r_WhatsApp%20Image%202026-04-14%20at%2013.30.14%20%282%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/1wrbpi5m_WhatsApp%20Image%202026-04-14%20at%2013.30.14.jpeg"
]

output_dir = "/app/frontend/public/images/properties/prop-dlf2-2"

start_index = 6  # Starting from gallery-6.jpg

for idx, url in enumerate(image_urls, start_index):
    try:
        print(f"Downloading image {idx}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        output_path = f"{output_dir}/gallery-{idx}.jpg"
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Saved: /images/properties/prop-dlf2-2/gallery-{idx}.jpg")
        
    except Exception as e:
        print(f"✗ Error processing image {idx}: {e}")

print(f"\n✅ Successfully downloaded 5 additional images (gallery-6 to gallery-10)")
