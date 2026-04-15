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
        "featured": True,
        "images": [
            "/images/properties/prop-sushant/gallery-1.jpg",
            "/images/properties/prop-sushant/gallery-2.jpg",
            "/images/properties/prop-sushant/gallery-3.jpg",
            "/images/properties/prop-sushant/gallery-4.jpg",
            "/images/properties/prop-sushant/gallery-5.jpg",
            "/images/properties/prop-sushant/gallery-6.jpg",
            "/images/properties/prop-sushant/gallery-7.jpg",
            "/images/properties/prop-sushant/gallery-8.jpg"
        ]
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
        "featured": True,
        "images": [
            "/images/properties/prop-malibu/gallery-1.jpg",
            "/images/properties/prop-malibu/gallery-2.jpg",
            "/images/properties/prop-malibu/gallery-3.jpg",
            "/images/properties/prop-malibu/gallery-4.jpg"
        ]
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
        "featured": True,
        "images": [
            "/images/properties/prop-sushant-c2/gallery-1.jpg",
            "/images/properties/prop-sushant-c2/gallery-2.jpg",
            "/images/properties/prop-sushant-c2/gallery-3.jpg",
            "/images/properties/prop-sushant-c2/gallery-4.jpg",
            "/images/properties/prop-sushant-c2/gallery-5.jpg",
            "/images/properties/prop-sushant-c2/gallery-6.jpg",
            "/images/properties/prop-sushant-c2/gallery-7.jpg",
            "/images/properties/prop-sushant-c2/gallery-8.jpg",
            "/images/properties/prop-sushant-c2/gallery-9.jpg",
            "/images/properties/prop-sushant-c2/gallery-10.jpg",
            "/images/properties/prop-sushant-c2/gallery-11.jpg"
        ]
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
    },
    {
        "id": "prop-dlf4",
        "title": "Luxury 4BHK Builder Floor - DLF Phase 4",
        "price": "Price on Request",
        "location": "DLF Phase 4, Gurugram",
        "sector": "DLF Phase 4",
        "size": "400 sq yds",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/ztfrga6c_WhatsApp%20Image%202026-04-11%20at%206.03.57%20PM.jpeg",
        "description": "Premium 4BHK builder floor in prestigious DLF Phase 4 with excellent amenities",
        "status": "available",
        "featured": True,
        "images": [
            "/images/properties/prop-dlf4/gallery-1.jpg",
            "/images/properties/prop-dlf4/gallery-2.jpg",
            "/images/properties/prop-dlf4/gallery-3.jpg",
            "/images/properties/prop-dlf4/gallery-4.jpg",
            "/images/properties/prop-dlf4/gallery-5.jpg",
            "/images/properties/prop-dlf4/gallery-6.jpg",
            "/images/properties/prop-dlf4/gallery-7.jpg",
            "/images/properties/prop-dlf4/gallery-8.jpg",
            "/images/properties/prop-dlf4/gallery-9.jpg",
            "/images/properties/prop-dlf4/gallery-10.jpg"
        ]
    },
    {
        "id": "prop-dlf2",
        "title": "Ultra Modern 4BHK Builder Floor - DLF Phase 2",
        "price": "Price on Request",
        "location": "DLF Phase 2, Gurugram",
        "sector": "DLF Phase 2",
        "size": "402 sq yds",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/2azxgacj_WhatsApp%20Image%202026-04-11%20at%206.02.32%20PM%20%281%29.jpeg",
        "description": "Contemporary 4BHK builder floor with stunning modern architecture in DLF Phase 2",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-dlf1",
        "title": "Premium 4BHK Builder Floor - DLF Phase 1",
        "price": "Price on Request",
        "location": "DLF Phase 1, Gurugram",
        "sector": "DLF Phase 1",
        "size": "500 sq yds",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/g3o4ni2i_WhatsApp%20Image%202026-04-11%20at%206.00.15%20PM.jpeg",
        "description": "Luxurious 4BHK builder floor with premium wooden cladding and modern design in DLF Phase 1",
        "status": "available",
        "featured": True,
        "images": [
            "/images/properties/prop-dlf1/gallery-1.jpg",
            "/images/properties/prop-dlf1/gallery-2.jpg",
            "/images/properties/prop-dlf1/gallery-3.jpg",
            "/images/properties/prop-dlf1/gallery-4.jpg",
            "/images/properties/prop-dlf1/gallery-5.jpg",
            "/images/properties/prop-dlf1/gallery-6.jpg",
            "/images/properties/prop-dlf1/gallery-7.jpg"
        ]
    },
    {
        "id": "prop-dlf2-2",
        "title": "Contemporary 4BHK Builder Floor - DLF Phase 2",
        "price": "Price on Request",
        "location": "DLF Phase 2, Gurugram",
        "sector": "DLF Phase 2",
        "size": "300 sq yds",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/1jehpiso_WhatsApp%20Image%202026-04-11%20at%205.59.00%20PM.jpeg",
        "description": "Modern 4BHK builder floor with contemporary design and lattice features in DLF Phase 2",
        "status": "available",
        "featured": True,
        "images": [
            "/images/properties/prop-dlf2-2/gallery-1.jpg",
            "/images/properties/prop-dlf2-2/gallery-2.jpg",
            "/images/properties/prop-dlf2-2/gallery-3.jpg",
            "/images/properties/prop-dlf2-2/gallery-4.jpg",
            "/images/properties/prop-dlf2-2/gallery-5.jpg",
            "/images/properties/prop-dlf2-2/gallery-6.jpg",
            "/images/properties/prop-dlf2-2/gallery-7.jpg",
            "/images/properties/prop-dlf2-2/gallery-8.jpg",
            "/images/properties/prop-dlf2-2/gallery-9.jpg",
            "/images/properties/prop-dlf2-2/gallery-10.jpg",
            "/images/properties/prop-dlf2-2/gallery-11.jpg",
            "/images/properties/prop-dlf2-2/gallery-12.jpg"
        ]
    },
    {
        "id": "prop-dlf2-sec27",
        "title": "Ultra Luxury 4BHK Builder Floor - DLF Phase 2, Sector 27",
        "price": "Price on Request",
        "location": "DLF Phase 2, Sector 27, Gurugram",
        "sector": "DLF Phase 2",
        "size": "300 sq yds",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/5ki9zmha_WhatsApp%20Image%202026-04-11%20at%205.58.19%20PM.jpeg",
        "description": "Premium 4BHK builder floor with wooden louver facade and stone cladding in DLF Phase 2, Sector 27",
        "status": "available",
        "featured": True,
        "images": [
            "/images/properties/prop-dlf2-sec27/gallery-1.jpg",
            "/images/properties/prop-dlf2-sec27/gallery-2.jpg",
            "/images/properties/prop-dlf2-sec27/gallery-3.jpg",
            "/images/properties/prop-dlf2-sec27/gallery-4.jpg"
        ]
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
