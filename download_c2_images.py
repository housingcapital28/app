import requests
import os

# Image URLs for prop-sushant-c2
image_urls = [
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/8hrrfouo_WhatsApp%20Image%202026-04-14%20at%2012.34.39%20PM%20%281%29.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/16pfb73p_WhatsApp%20Image%202026-04-14%20at%2012.34.39%20PM.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/43djh9s1_WhatsApp%20Image%202026-04-14%20at%2012.34.40%20PM.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/v72h3y8b_WhatsApp%20Image%202026-04-14%20at%2012.34.42%20PM.jpeg",
    "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/p9i4hpsr_WhatsApp%20Image%202026-04-14%20at%2012.34.44%20PM%20%281%29.jpeg"
]

output_dir = "/app/frontend/public/images/properties/prop-sushant-c2"
os.makedirs(output_dir, exist_ok=True)

converted_paths = []

for idx, url in enumerate(image_urls, 1):
    try:
        print(f"Downloading image {idx}/{len(image_urls)}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Save as JPG
        output_path = f"{output_dir}/gallery-{idx}.jpg"
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        # Store the relative path for frontend
        relative_path = f"/images/properties/prop-sushant-c2/gallery-{idx}.jpg"
        converted_paths.append(relative_path)
        
        print(f"✓ Saved: {relative_path}")
        
    except Exception as e:
        print(f"✗ Error processing image {idx}: {e}")

print(f"\n✅ Successfully downloaded {len(converted_paths)} images")
print("\nImage paths:")
for path in converted_paths:
    print(f"  {path}")
