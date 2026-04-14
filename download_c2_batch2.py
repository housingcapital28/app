import requests
import os

# Additional 5 images for prop-sushant-c2
image_urls = [
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/o1s3155p_WhatsApp%20Image%202026-04-14%20at%2012.34.44%20PM%20%283%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/83lzcu0v_WhatsApp%20Image%202026-04-14%20at%2012.34.43%20PM%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/v6eu6eyq_WhatsApp%20Image%202026-04-14%20at%2012.34.43%20PM.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/3t9ya7hs_WhatsApp%20Image%202026-04-14%20at%2012.34.44%20PM%20%282%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/pb61mk9l_WhatsApp%20Image%202026-04-14%20at%2012.34.44%20PM%20%281%29.jpeg"
]

output_dir = "/app/frontend/public/images/properties/prop-sushant-c2"

start_index = 7  # Starting from gallery-7.jpg

for idx, url in enumerate(image_urls, start_index):
    try:
        print(f"Downloading image {idx}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        output_path = f"{output_dir}/gallery-{idx}.jpg"
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Saved: /images/properties/prop-sushant-c2/gallery-{idx}.jpg")
        
    except Exception as e:
        print(f"✗ Error processing image {idx}: {e}")

print(f"\n✅ Successfully downloaded 5 additional images (gallery-7 to gallery-11)")
