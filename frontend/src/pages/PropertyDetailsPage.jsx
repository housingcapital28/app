import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Button } from '../components/ui/button';
import { Card, CardContent } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Separator } from '../components/ui/separator';
import { 
  ArrowLeft, 
  MapPin, 
  Maximize, 
  Bed, 
  Bath, 
  Phone, 
  MessageCircle,
  Home,
  CheckCircle
} from 'lucide-react';
import { getProperty } from '../api/api';
import { Navbar } from '../components/Navbar';
import { Footer } from '../components/Footer';

export const PropertyDetailsPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [property, setProperty] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProperty = async () => {
      try {
        setLoading(true);
        const data = await getProperty(id);
        setProperty(data);
      } catch (err) {
        console.error('Error loading property:', err);
      } finally {
        setLoading(false);
      }
    };

    if (id) {
      fetchProperty();
    }
  }, [id]);

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50">
        <Navbar />
        <div className="container mx-auto px-4 py-32 text-center">
          <div className="animate-pulse">
            <div className="h-12 bg-slate-300 rounded w-64 mx-auto"></div>
          </div>
        </div>
      </div>
    );
  }

  if (!property) {
    return (
      <div className="min-h-screen bg-slate-50">
        <Navbar />
        <div className="container mx-auto px-4 py-32 text-center">
          <h2 className="text-2xl font-bold text-slate-900 mb-4">Property Not Found</h2>
          <Button onClick={() => navigate('/')}>Back to Home</Button>
        </div>
      </div>
    );
  }

  const whatsappMessage = `Hello Housing Capital, I'm interested in the ${property.type} at ${property.location}. Please provide more details.`;
  const whatsappUrl = `https://wa.me/918742932997?text=${encodeURIComponent(whatsappMessage)}`;

  return (
    <div className="min-h-screen bg-slate-50">
      <Navbar />
      
      {/* Hero Image Section */}
      <section className="relative h-96 md:h-[500px] mt-24">
        <img
          src={property.image}
          alt={property.title}
          className="w-full h-full object-cover"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-slate-900/60 to-transparent"></div>
        
        {/* Property Type Badge */}
        <div className="absolute top-6 left-6">
          <Badge className="bg-amber-600 text-white px-4 py-2 text-lg">
            {property.type}
          </Badge>
        </div>

        {/* Back Button */}
        <div className="absolute top-6 right-6">
          <Button
            onClick={() => navigate('/')}
            className="bg-white text-slate-900 hover:bg-slate-100"
          >
            <ArrowLeft className="w-4 h-4 mr-2" />
            Back to Listings
          </Button>
        </div>
      </section>

      {/* Property Details Section */}
      <section className="container mx-auto px-4 py-12">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="lg:col-span-2">
            {/* Property Header */}
            <div className="mb-8">
              <h1 className="text-4xl md:text-5xl font-bold text-slate-900 mb-4">
                {property.title}
              </h1>
              
              <div className="flex items-center gap-2 text-slate-600 mb-6">
                <MapPin className="w-5 h-5 text-amber-600" />
                <span className="text-xl">{property.location}</span>
              </div>

              <div className="text-3xl font-bold text-amber-600 mb-6">
                {property.price}
              </div>
            </div>

            <Separator className="mb-8" />

            {/* Property Specifications */}
            <div className="mb-8">
              <h2 className="text-2xl font-bold text-slate-900 mb-6">Property Details</h2>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                <Card className="border-slate-200">
                  <CardContent className="p-6 text-center">
                    <Maximize className="w-8 h-8 text-amber-600 mx-auto mb-3" />
                    <div className="text-sm text-slate-600 mb-1">Plot Size</div>
                    <div className="text-lg font-bold text-slate-900">{property.size}</div>
                  </CardContent>
                </Card>

                {property.bedrooms && (
                  <Card className="border-slate-200">
                    <CardContent className="p-6 text-center">
                      <Bed className="w-8 h-8 text-amber-600 mx-auto mb-3" />
                      <div className="text-sm text-slate-600 mb-1">Bedrooms</div>
                      <div className="text-lg font-bold text-slate-900">{property.bedrooms} BHK</div>
                    </CardContent>
                  </Card>
                )}

                {property.bathrooms && (
                  <Card className="border-slate-200">
                    <CardContent className="p-6 text-center">
                      <Bath className="w-8 h-8 text-amber-600 mx-auto mb-3" />
                      <div className="text-sm text-slate-600 mb-1">Bathrooms</div>
                      <div className="text-lg font-bold text-slate-900">{property.bathrooms}</div>
                    </CardContent>
                  </Card>
                )}

                <Card className="border-slate-200">
                  <CardContent className="p-6 text-center">
                    <Home className="w-8 h-8 text-amber-600 mx-auto mb-3" />
                    <div className="text-sm text-slate-600 mb-1">Type</div>
                    <div className="text-lg font-bold text-slate-900">{property.type}</div>
                  </CardContent>
                </Card>
              </div>
            </div>

            <Separator className="mb-8" />

            {/* Description */}
            <div className="mb-8">
              <h2 className="text-2xl font-bold text-slate-900 mb-4">Description</h2>
              <p className="text-slate-700 leading-relaxed text-lg">
                {property.description || `Premium ${property.type} located in ${property.location}. This property offers excellent connectivity and modern amenities. Perfect for families looking for a comfortable and luxurious living space in Gurugram.`}
              </p>
            </div>

            <Separator className="mb-8" />

            {/* Key Features */}
            <div className="mb-8">
              <h2 className="text-2xl font-bold text-slate-900 mb-4">Key Features</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {[
                  'Prime Location in Gurugram',
                  'Modern Architecture',
                  'Well Ventilated Spaces',
                  'Ample Parking Space',
                  'Close to Schools & Markets',
                  'Easy Connectivity',
                  'Gated Community',
                  'Power Backup'
                ].map((feature, index) => (
                  <div key={index} className="flex items-center gap-3">
                    <CheckCircle className="w-5 h-5 text-green-600 flex-shrink-0" />
                    <span className="text-slate-700">{feature}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Sidebar - Contact Card */}
          <div className="lg:col-span-1">
            <Card className="border-slate-200 sticky top-32">
              <CardContent className="p-6">
                <h3 className="text-xl font-bold text-slate-900 mb-4">Interested in this property?</h3>
                <p className="text-slate-600 mb-6">
                  Contact us for more details and schedule a site visit.
                </p>

                {/* WhatsApp Button */}
                <a href={whatsappUrl} target="_blank" rel="noopener noreferrer" className="block mb-3">
                  <Button className="w-full bg-green-600 hover:bg-green-700 text-white py-6 text-lg">
                    <MessageCircle className="w-5 h-5 mr-2" />
                    Chat on WhatsApp
                  </Button>
                </a>

                {/* Call Button */}
                <a href="tel:+918742932997" className="block mb-6">
                  <Button className="w-full bg-amber-600 hover:bg-amber-700 text-white py-6 text-lg">
                    <Phone className="w-5 h-5 mr-2" />
                    Call Now
                  </Button>
                </a>

                <Separator className="mb-6" />

                {/* Contact Info */}
                <div className="space-y-3 text-sm">
                  <div>
                    <div className="text-slate-600 mb-1">Phone</div>
                    <div className="font-semibold text-slate-900">87429 32997</div>
                  </div>
                  <div>
                    <div className="text-slate-600 mb-1">Location</div>
                    <div className="font-semibold text-slate-900">{property.sector}, Gurugram</div>
                  </div>
                  <div>
                    <div className="text-slate-600 mb-1">Property ID</div>
                    <div className="font-semibold text-slate-900">{property.id}</div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      <Footer />
    </div>
  );
};
