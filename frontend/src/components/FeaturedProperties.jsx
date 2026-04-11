import React from 'react';
import { PropertyCard } from './PropertyCard';
import { featuredProperties } from '../data/mock';

export const FeaturedProperties = () => {
  return (
    <section id="properties" className="py-20 bg-slate-50">
      <div className="container mx-auto px-4">
        {/* Section Header */}
        <div className="text-center mb-12">
          <h2 className="text-4xl md:text-5xl font-bold text-slate-900 mb-4">
            Featured Properties
          </h2>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            Handpicked premium properties in prime Gurugram locations
          </p>
        </div>

        {/* Properties Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {featuredProperties.map((property) => (
            <PropertyCard key={property.id} property={property} />
          ))}
        </div>
      </div>
    </section>
  );
};
