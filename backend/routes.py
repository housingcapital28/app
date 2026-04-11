from fastapi import APIRouter, HTTPException
from typing import List
from models import (
    Property, PropertyCreate, PropertySearch,
    Project, ProjectCreate,
    Lead, LeadCreate,
    Testimonial, TestimonialCreate
)
from motor.motor_asyncio import AsyncIOMotorClient
import os

router = APIRouter()

# Get database connection from server.py
def get_db():
    from server import db
    return db


# Property Routes
@router.get("/properties", response_model=List[Property])
async def get_properties():
    """Get all featured properties"""
    try:
        db = get_db()
        properties = await db.properties.find({"featured": True}).to_list(100)
        return [Property(**prop) for prop in properties]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/properties/{property_id}", response_model=Property)
async def get_property(property_id: str):
    """Get single property by ID"""
    try:
        db = get_db()
        property_data = await db.properties.find_one({"id": property_id})
        if not property_data:
            raise HTTPException(status_code=404, detail="Property not found")
        return Property(**property_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/properties/search", response_model=List[Property])
async def search_properties(search: PropertySearch):
    """Search properties with filters"""
    try:
        db = get_db()
        query = {"featured": True}
        
        if search.location:
            query["sector"] = {"$regex": search.location, "$options": "i"}
        
        if search.property_type:
            query["type"] = search.property_type
        
        # Budget filter - simplified for MVP
        if search.budget:
            # This is a simple implementation
            # In production, you'd convert price strings to numbers for proper comparison
            pass
        
        properties = await db.properties.find(query).to_list(100)
        return [Property(**prop) for prop in properties]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/properties", response_model=Property)
async def create_property(property_data: PropertyCreate):
    """Create a new property (admin endpoint)"""
    try:
        db = get_db()
        property_obj = Property(**property_data.dict())
        await db.properties.insert_one(property_obj.dict())
        return property_obj
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Project Routes
@router.get("/projects", response_model=List[Project])
async def get_projects():
    """Get all ongoing projects"""
    try:
        db = get_db()
        projects = await db.projects.find().to_list(100)
        return [Project(**proj) for proj in projects]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/projects", response_model=Project)
async def create_project(project_data: ProjectCreate):
    """Create a new project (admin endpoint)"""
    try:
        db = get_db()
        project_obj = Project(**project_data.dict())
        await db.projects.insert_one(project_obj.dict())
        return project_obj
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Lead Routes
@router.post("/leads", response_model=Lead)
async def create_lead(lead_data: LeadCreate):
    """Submit a new inquiry/lead"""
    try:
        db = get_db()
        lead_obj = Lead(**lead_data.dict())
        await db.leads.insert_one(lead_obj.dict())
        return lead_obj
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/leads", response_model=List[Lead])
async def get_leads():
    """Get all leads (admin endpoint)"""
    try:
        db = get_db()
        leads = await db.leads.find().sort("created_at", -1).to_list(1000)
        return [Lead(**lead) for lead in leads]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Testimonial Routes
@router.get("/testimonials", response_model=List[Testimonial])
async def get_testimonials():
    """Get all approved testimonials"""
    try:
        db = get_db()
        testimonials = await db.testimonials.find({"approved": True}).to_list(100)
        return [Testimonial(**test) for test in testimonials]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/testimonials", response_model=Testimonial)
async def create_testimonial(testimonial_data: TestimonialCreate):
    """Create a new testimonial (admin endpoint)"""
    try:
        db = get_db()
        testimonial_obj = Testimonial(**testimonial_data.dict())
        await db.testimonials.insert_one(testimonial_obj.dict())
        return testimonial_obj
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
