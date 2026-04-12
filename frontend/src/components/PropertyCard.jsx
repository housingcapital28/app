import React from 'react';
import { Card, CardContent } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { MapPin, Maximize, Bed, Bath } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export const PropertyCard = ({ property }) => {
  const navigate = useNavigate();

  const handleViewDetails = () => {
    navigate(`/property/${property.id}`);
  };

  return (
    <Card className="overflow-hidden hover:shadow-xl transition-all duration-300 group border-slate-200">
      {/* Image */}
      <div className="relative h-56 overflow-hidden">
        <img
          src={property.image}
          alt={property.location}
          className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
        />
        <div className="absolute top-4 left-4">
          <Badge className="bg-amber-600 hover:bg-amber-700 text-white px-3 py-1">
            {property.type}
          </Badge>
        </div>
        <div className="absolute top-4 right-4">
          <Badge className="bg-white text-slate-900 px-3 py-1 font-bold">
            {property.price}
          </Badge>
        </div>
      </div>

      {/* Content */}
      <CardContent className="p-5">
        {/* Location */}
        <div className="flex items-start mb-3">
          <MapPin className="w-4 h-4 text-amber-600 mr-2 mt-1 flex-shrink-0" />
          <h3 className="text-lg font-semibold text-slate-900">{property.location}</h3>
        </div>

        {/* Details */}
        <div className="flex items-center gap-4 mb-4 text-sm text-slate-600">
          <div className="flex items-center">
            <Maximize className="w-4 h-4 mr-1" />
            <span>{property.size}</span>
          </div>
          {property.bedrooms && (
            <div className="flex items-center">
              <Bed className="w-4 h-4 mr-1" />
              <span>{property.bedrooms} BHK</span>
            </div>
          )}
          {property.bathrooms && (
            <div className="flex items-center">
              <Bath className="w-4 h-4 mr-1" />
              <span>{property.bathrooms}</span>
            </div>
          )}
        </div>

        {/* Button */}
        <Button
          onClick={handleViewDetails}
          className="w-full bg-slate-900 hover:bg-amber-600 text-white transition-colors duration-300"
        >
          View Details
        </Button>
      </CardContent>
    </Card>
  );
};
