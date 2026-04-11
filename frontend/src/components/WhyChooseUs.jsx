import React from 'react';
import { Card, CardContent } from './ui/card';
import { BadgeCheck, MapPin, Handshake, TrendingUp } from 'lucide-react';
import { whyChooseUs } from '../data/mock';

const iconMap = {
  BadgeCheck: BadgeCheck,
  MapPin: MapPin,
  HandshakeIcon: Handshake,
  TrendingUp: TrendingUp
};

export const WhyChooseUs = () => {
  return (
    <section id="about" className="py-20 bg-white">
      <div className="container mx-auto px-4">
        {/* Section Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-slate-900 mb-4">
            Why Choose Housing Capital
          </h2>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            Your trusted partner in Gurugram real estate with proven expertise
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {whyChooseUs.map((feature) => {
            const Icon = iconMap[feature.icon];
            return (
              <Card
                key={feature.id}
                className="border-slate-200 hover:border-amber-600 transition-all duration-300 hover:shadow-lg group"
              >
                <CardContent className="p-8 text-center">
                  {/* Icon */}
                  <div className="w-16 h-16 bg-amber-100 rounded-full flex items-center justify-center mx-auto mb-5 group-hover:bg-amber-600 transition-colors duration-300">
                    <Icon className="w-8 h-8 text-amber-600 group-hover:text-white transition-colors duration-300" />
                  </div>

                  {/* Title */}
                  <h3 className="text-xl font-bold text-slate-900 mb-3">
                    {feature.title}
                  </h3>

                  {/* Description */}
                  <p className="text-slate-600 leading-relaxed">
                    {feature.description}
                  </p>
                </CardContent>
              </Card>
            );
          })}
        </div>
      </div>
    </section>
  );
};
