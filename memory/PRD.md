# Housing Capital - Real Estate Website PRD

## Original Problem Statement
Create a modern, premium real estate website for Housing Capital, a Gurugram-based real estate company dealing in luxury floors, builder floors, plots, and investment properties. Design style inspired by Zillow homepage layout with large hero section, bold heading, property search bar, clean white layout, and professional real estate visuals.

## User Personas
1. **Property Buyers**: Looking for builder floors, apartments, plots in Gurugram
2. **Property Sellers**: Want to sell their properties through trusted advisors
3. **Investors**: Seeking high ROI investment opportunities in Gurugram real estate
4. **Renters**: Looking for rental properties in premium locations

## Core Requirements
- Premium, clean, white theme with professional real estate UI
- Zillow-inspired layout and design
- Mobile responsive and optimized
- WhatsApp integration for lead generation
- Property search functionality
- Featured properties showcase
- Ongoing projects display
- Client testimonials
- Multi-section landing page

## Architecture
- **Frontend**: React with Vite, Tailwind CSS, shadcn/ui components
- **Backend**: FastAPI (Python), MongoDB
- **Deployment**: Emergent platform

## Contact Information
- Phone: 87429 32997
- WhatsApp: wa.me/918742932997
- Location: Gurugram, Haryana, India
- Email: info@housingcapital.in

---

## What's Been Implemented (Dec 2024)

### ✅ Phase 1 - Frontend with Mock Data (Completed)

**Date**: December 2024

#### Components Created:
1. **Navbar Component** (`/app/frontend/src/components/Navbar.jsx`)
   - Sticky navigation with smooth scroll
   - Mobile responsive menu
   - Contact button with phone number
   - Menu items: Home, Buy Property, Sell Property, Projects, Investment Deals, About Us, Contact

2. **Hero Section** (`/app/frontend/src/components/HeroSection.jsx`)
   - Full-width background with luxury property image
   - Bold headline: "Buy. Sell. Invest. With Confidence."
   - Property search bar with:
     - Location dropdown (Gurugram sectors)
     - Property Type dropdown
     - Budget dropdown
     - Search button
   - CTA buttons: Contact Now, Chat on WhatsApp

3. **Featured Properties** (`/app/frontend/src/components/FeaturedProperties.jsx`)
   - Grid layout (3 columns on desktop, responsive)
   - 9 premium property listings with mock data
   - Property cards showing: image, price, location, size, BHK, bathrooms

4. **Property Card** (`/app/frontend/src/components/PropertyCard.jsx`)
   - Hover effects with image zoom
   - Badge for property type
   - Price display
   - Property details (sqft, BHK, bathrooms)
   - View Details button

5. **Why Choose Us** (`/app/frontend/src/components/WhyChooseUs.jsx`)
   - 4 feature cards:
     - Verified Listings
     - Local Area Expertise
     - End-to-End Assistance
     - High ROI Investment Deals
   - Hover effects with icon color transitions

6. **Ongoing Projects** (`/app/frontend/src/components/OngoingProjects.jsx`)
   - 3 project cards with construction images
   - Project details: name, location, description, units, status
   - Status badges: Under Construction, Booking Open, Pre-Launch

7. **Testimonials** (`/app/frontend/src/components/Testimonials.jsx`)
   - 3 client testimonials
   - 5-star ratings
   - Client names, locations, dates

8. **CTA Section** (`/app/frontend/src/components/CTASection.jsx`)
   - Strong call-to-action: "Looking to Buy, Sell or Rent in Gurugram?"
   - Call Now button (tel:+918742932997)
   - WhatsApp button with pre-filled message
   - Contact info and availability hours

9. **Footer** (`/app/frontend/src/components/Footer.jsx`)
   - Company info with branding
   - Quick links navigation
   - Property types list
   - Contact information
   - Social media icons (Facebook, Instagram, LinkedIn, YouTube)
   - WhatsApp button
   - Copyright notice

10. **Home Page** (`/app/frontend/src/pages/HomePage.jsx`)
    - Main page component integrating all sections

#### Mock Data (`/app/frontend/src/data/mock.js`)
- 9 featured properties with realistic Gurugram data
- 3 ongoing projects
- 4 "Why Choose Us" features
- 3 client testimonials
- Gurugram sectors list
- Property types
- Budget ranges

#### Design Features Implemented:
- ✅ Professional real estate color palette (white, amber/gold accents, dark navy)
- ✅ Lucide-react icons (no emoji icons)
- ✅ Smooth hover transitions and micro-animations
- ✅ Mobile responsive design
- ✅ Clean white theme with premium look
- ✅ WhatsApp integration for leads
- ✅ Zillow-inspired layout
- ✅ Fixed hero background with parallax effect
- ✅ Shadcn UI components (Button, Card, Badge, Select, Separator)

---

## Prioritized Backlog

### P0 - Critical Features (Backend Development)
1. **Database Models**
   - Property model (id, title, price, location, size, type, bedrooms, bathrooms, images, description, status)
   - Project model (id, name, location, description, units, status, images)
   - Inquiry/Lead model (name, email, phone, message, property_id, timestamp)
   - Testimonial model (name, location, rating, text, date)

2. **Backend API Endpoints**
   - `GET /api/properties` - Fetch all properties
   - `GET /api/properties/:id` - Get single property details
   - `POST /api/properties/search` - Search properties by location, type, budget
   - `GET /api/projects` - Fetch ongoing projects
   - `POST /api/leads` - Submit inquiry/lead form
   - `GET /api/testimonials` - Fetch testimonials

3. **Frontend-Backend Integration**
   - Remove mock.js data
   - Connect property listings to backend API
   - Connect search functionality to backend
   - Connect lead/contact forms to backend
   - Add loading states and error handling

### P1 - Important Features
4. **Property Details Page**
   - Individual property page with full details
   - Image gallery/carousel
   - Property specifications
   - Location map
   - Contact form for property

5. **Contact/Lead Forms**
   - Contact form in hero section
   - Property inquiry form
   - Phone number validation
   - Email notifications on form submission

6. **Admin Panel**
   - Add/Edit/Delete properties
   - Manage projects
   - View leads/inquiries
   - Authentication for admin

### P2 - Nice to Have Features
7. **Advanced Search & Filters**
   - Filter by price range, size, BHK
   - Sort by price, date, popularity
   - Save searches

8. **Property Comparison**
   - Compare multiple properties side by side

9. **User Accounts**
   - Save favorite properties
   - Property alerts
   - View inquiry history

10. **Enhanced Features**
    - Property location on Google Maps
    - Virtual tour integration
    - EMI calculator
    - WhatsApp direct property share
    - Email property details

---

## Next Tasks

### Immediate Next Steps:
1. ✅ **Frontend complete with mock data** - User can preview the site immediately
2. **Await user approval** for moving to backend development
3. **Backend development** - API endpoints and database models
4. **Frontend-Backend integration** - Replace mock data with real API calls
5. **Testing** - End-to-end testing with testing agent
6. **Deployment optimizations**

### Future Enhancements:
- SEO optimization (meta tags, structured data)
- Blog section for real estate insights
- Property video tours
- Advanced analytics
- Multi-language support (Hindi/English)
- Payment gateway integration for booking

---

## Technical Stack
- **Frontend**: React 19, React Router, Tailwind CSS, shadcn/ui, Axios
- **Backend**: FastAPI, Motor (MongoDB async driver), Pydantic
- **Database**: MongoDB
- **Icons**: Lucide React
- **Deployment**: Emergent platform

## Design Guidelines Followed
- No dark colorful gradients
- No emoji icons (using Lucide React)
- Professional real estate color palette
- Smooth transitions for interactive elements
- Mobile-first responsive design
- Named exports for components
- Clean white premium theme
