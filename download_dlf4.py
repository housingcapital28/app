import requests
import os

# 5 images for prop-dlf4
image_urls = [
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/mnpfawfw_WhatsApp%20Image%202026-04-14%20at%2013.28.37.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/vv3rtmo0_WhatsApp%20Image%202026-04-14%20at%2013.28.38%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/5luapz4x_WhatsApp%20Image%202026-04-14%20at%2013.28.38%20%282%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/3z8o1ssm_WhatsApp%20Image%202026-04-14%20at%2013.28.38.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/9503udm0_WhatsApp%20Image%202026-04-14%20at%2013.28.39%20%281%29.jpeg"
]

output_dir = "/app/frontend/public/images/properties/prop-dlf4"

for idx, url in enumerate(image_urls, 1):
    try:
        print(f"Downloading image {idx}/5...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        output_path = f"{output_dir}/gallery-{idx}.jpg"
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Saved: /images/properties/prop-dlf4/gallery-{idx}.jpg")
        
    except Exception as e:
        print(f"✗ Error processing image {idx}: {e}")

print(f"\n✅ Successfully downloaded 5 images for prop-dlf4")
