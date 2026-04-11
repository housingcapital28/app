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
        "title": "Premium 3BHK Builder Floor",
        "price": "Price on Request",
        "location": "Sushant Lok C Block, Sector 43, Gurugram",
        "sector": "Sector 43",
        "size": "215 sq yds",
        "type": "Builder Floor",
        "bedrooms": 3,
        "bathrooms": 3,
        "image": "https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/5ja2obca_IMG_7953.jpg",
        "description": "Beautiful 3BHK builder floor in Sushant Lok C Block with excellent location",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-1",
        "title": "Luxury 4BHK Builder Floor",
        "price": "₹2.5 Cr",
        "location": "Sector 57, Gurugram",
        "sector": "Sector 57",
        "size": "2400 sqft",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://images.unsplash.com/photo-1680919838857-d54e011093d3",
        "description": "Premium 4BHK builder floor in the heart of Sector 57 with modern amenities",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-2",
        "title": "Modern 3BHK Apartment",
        "price": "₹1.8 Cr",
        "location": "Sector 82, Gurugram",
        "sector": "Sector 82",
        "size": "1850 sqft",
        "type": "Apartment",
        "bedrooms": 3,
        "bathrooms": 3,
        "image": "https://images.unsplash.com/photo-1648502298359-055a3f374705",
        "description": "Contemporary apartment with excellent connectivity",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-3",
        "title": "Luxurious 4BHK Floor",
        "price": "₹3.2 Cr",
        "location": "Golf Course Road, Gurugram",
        "sector": "Golf Course Road",
        "size": "3100 sqft",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 5,
        "image": "https://images.pexels.com/photos/565324/pexels-photo-565324.jpeg",
        "description": "Premium builder floor on Golf Course Road",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-4",
        "title": "Affordable 3BHK Apartment",
        "price": "₹1.2 Cr",
        "location": "Sector 95, Gurugram",
        "sector": "Sector 95",
        "size": "1500 sqft",
        "type": "Apartment",
        "bedrooms": 3,
        "bathrooms": 2,
        "image": "https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg",
        "description": "Well-designed 3BHK apartment in upcoming sector",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-5",
        "title": "Premium Plot",
        "price": "₹95 Lac",
        "location": "Sector 89, Gurugram",
        "sector": "Sector 89",
        "size": "250 sq yards",
        "type": "Plot",
        "bedrooms": None,
        "bathrooms": None,
        "image": "https://images.unsplash.com/photo-1650363700594-8e149ed80eec",
        "description": "Prime plot in residential sector",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-6",
        "title": "Spacious 4BHK Floor",
        "price": "₹2.8 Cr",
        "location": "Sector 54, Gurugram",
        "sector": "Sector 54",
        "size": "2800 sqft",
        "type": "Builder Floor",
        "bedrooms": 4,
        "bathrooms": 4,
        "image": "https://images.unsplash.com/photo-1565363887715-8884629e09ee",
        "description": "Spacious builder floor with modern amenities",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-7",
        "title": "Ultra Luxury 5BHK",
        "price": "₹4.5 Cr",
        "location": "DLF Phase 5, Gurugram",
        "sector": "DLF Phase 5",
        "size": "3800 sqft",
        "type": "Apartment",
        "bedrooms": 5,
        "bathrooms": 5,
        "image": "https://images.pexels.com/photos/29027284/pexels-photo-29027284.jpeg",
        "description": "Ultra luxury apartment in prestigious DLF Phase 5",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-8",
        "title": "Premium 5BHK Builder Floor",
        "price": "₹6.2 Cr",
        "location": "Golf Course Extension Road",
        "sector": "Golf Course Extension Road",
        "size": "4500 sqft",
        "type": "Builder Floor",
        "bedrooms": 5,
        "bathrooms": 6,
        "image": "https://images.unsplash.com/photo-1610526662524-bd113e746fdb",
        "description": "Exceptional builder floor with premium finishes",
        "status": "available",
        "featured": True
    },
    {
        "id": "prop-9",
        "title": "Comfortable 3BHK",
        "price": "₹1.5 Cr",
        "location": "Sector 70, Gurugram",
        "sector": "Sector 70",
        "size": "1650 sqft",
        "type": "Apartment",
        "bedrooms": 3,
        "bathrooms": 3,
        "image": "https://images.pexels.com/photos/18587809/pexels-photo-18587809.jpeg",
        "description": "Well-maintained 3BHK apartment",
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
