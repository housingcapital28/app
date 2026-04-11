import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]


# Seed data based on mock.js
properties_seed = [
    {
        "id": "prop-sushant",
        "title": "Premium 4BHK Builder Floor",
        "price": "Price on Request",
        "location": "Sushant Lok C Block, Sector 43, Gurugram",
        "sector": "Sector 43",
        "size": "215 sq yds",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/5ja2obca_IMG_7953.jpg",
        "description": "Beautiful 4BHK builder floor in Sushant Lok C Block with excellent location",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-malibu",
        "title": "Corner Property 4BHK - Malibu Town",
        "price": "Price on Request",
        "location": "Malibu Town, Sector 48, Gurugram",
        "sector": "Sector 48",
        "size": "500 sq yds",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/xzokp3f5_WhatsApp%20Image%202026-04-11%20at%205.55.19%20PM.jpeg",
        "description": "Prime corner 4BHK builder floor in Malibu Town with excellent construction",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-sushant-c2",
        "title": "Luxury 4BHK Builder Floor",
        "price": "Price on Request",
        "location": "Sushant Lok C2 Block, Sector 43, Gurugram",
        "sector": "Sector 43",
        "size": "458 sq yds",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/3gjhkxd0_WhatsApp%20Image%202026-04-11%20at%205.57.37%20PM.jpeg",
        "description": "Spacious 4BHK builder floor in Sushant Lok C2 Block with modern amenities",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-sec23",
        "title": "Modern 4BHK Builder Floor",
        "price": "Price on Request",
        "location": "Sector 23, Gurugram",
        "sector": "Sector 23",
        "size": "342 sq yds",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/7fq6rh6i_WhatsApp%20Image%202026-04-11%20at%206.05.32%20PM.jpeg",
        "description": "Contemporary 4BHK builder floor in prime Sector 23 location",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-sec23-2",
        "title": "Premium 4BHK Builder Floor",
        "price": "Price on Request",
        "location": "Sector 23, Gurugram",
        "sector": "Sector 23",
        "size": "300 sq yds",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/kejl3gva_WhatsApp%20Image%202026-04-11%20at%206.04.42%20PM.jpeg",
        "description": "Elegant 4BHK builder floor with modern design in Sector 23",
        "status": "available",
        "featured": True
    }
]

projects_seed = [
    {
        "id": "proj-1",
        "name": "Housing Capital Heights",
        "location": "Sector 75, Gurugram",
        "description": "Premium 4BHK builder floors with modern amenities. Expected completion: Dec 2025",
        "units": "24 Units",
        "status": "Under Construction",
        "image": "https://images.unsplash.com/photo-1706437524158-6ca925ce5a06"
    },
    {
        "id": "proj-2",
        "name": "The Luxury Enclave",
        "location": "Golf Course Road, Gurugram",
        "description": "Exclusive gated community with 5BHK floors. Premium location with high ROI potential",
        "units": "16 Units",
        "status": "Booking Open",
        "image": "https://images.unsplash.com/photo-1485083269755-a7b559a4fe5e"
    },
    {
        "id": "proj-3",
        "name": "Capital Residency",
        "location": "Sector 82, Gurugram",
        "description": "3BHK & 4BHK luxury apartments with world-class amenities and prime connectivity",
        "units": "48 Units",
        "status": "Pre-Launch",
        "image": "https://images.pexels.com/photos/5335017/pexels-photo-5335017.jpeg"
    }
]

testimonials_seed = [
    {
        "id": "test-1",
        "name": "Rajesh Sharma",
        "location": "Sector 57, Gurugram",
        "rating": 5,
        "text": "Housing Capital helped us find our dream home. Their professionalism and knowledge of Gurugram market is exceptional. Highly recommended!",
        "date": "March 2024",
        "approved": True
    },
    {
        "id": "test-2",
        "name": "Priya Malhotra",
        "location": "Golf Course Road",
        "rating": 5,
        "text": "Sold my builder floor through Housing Capital in just 3 weeks at the best market price. Their end-to-end service made the entire process smooth.",
        "date": "February 2024",
        "approved": True
    },
    {
        "id": "test-3",
        "name": "Amit Verma",
        "location": "Sector 82, Gurugram",
        "rating": 5,
        "text": "Invested in two properties through Housing Capital. The ROI has been outstanding. They truly understand investment real estate.",
        "date": "January 2024",
        "approved": True
    }
]


async def seed_database():
    """Seed the database with initial data"""
    try:
        # Clear existing data
        await db.properties.delete_many({})
        await db.projects.delete_many({})
        await db.testimonials.delete_many({})
        
        # Insert seed data
        if properties_seed:
            await db.properties.insert_many(properties_seed)
            print(f"✓ Inserted {len(properties_seed)} properties")
        
        if projects_seed:
            await db.projects.insert_many(projects_seed)
            print(f"✓ Inserted {len(projects_seed)} projects")
        
        if testimonials_seed:
            await db.testimonials.insert_many(testimonials_seed)
            print(f"✓ Inserted {len(testimonials_seed)} testimonials")
        
        print("✓ Database seeded successfully!")
        
    except Exception as e:
        print(f"✗ Error seeding database: {str(e)}")
    finally:
        client.close()


if __name__ == "__main__":
    asyncio.run(seed_database())
