from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import uuid


class Property(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    price: str
    location: str
    sector: str
    size: str
    type: str
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    image: str
    images: List[str] = []  # Gallery images
    description: Optional[str] = None
    status: str = "available"
    featured: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)


class PropertyCreate(BaseModel):
    title: str
    price: str
    location: str
    sector: str
    size: str
    type: str
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    image: str
    images: List[str] = []  # Gallery images
    description: Optional[str] = None
    status: str = "available"
    featured: bool = True


class PropertySearch(BaseModel):
    location: Optional[str] = None
    property_type: Optional[str] = None
    budget: Optional[str] = None


class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    location: str
    description: str
    units: str
    status: str
    image: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ProjectCreate(BaseModel):
    name: str
    location: str
    description: str
    units: str
    status: str
    image: str


class Lead(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    phone: str
    message: str
    property_id: Optional[str] = None
    source: str = "website"
    created_at: datetime = Field(default_factory=datetime.utcnow)


class LeadCreate(BaseModel):
    name: str
    email: str
    phone: str
    message: str
    property_id: Optional[str] = None
    source: str = "website"


class Testimonial(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    location: str
    rating: int = 5
    text: str
    date: str
    approved: bool = True


class TestimonialCreate(BaseModel):
    name: str
    location: str
    rating: int = 5
    text: str
    date: str
    approved: bool = True
