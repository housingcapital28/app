import React, { useState } from 'react';
import { Button } from './ui/button';
import { Search } from 'lucide-react';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from './ui/select';
import { gurugramSectors, propertyTypes, budgetRanges } from '../data/mock';
import { searchProperties } from '../api/api';

export const HeroSection = () => {
  const [searchParams, setSearchParams] = useState({
    location: '',
    property_type: '',
    budget: ''
  });
  const [searching, setSearching] = useState(false);

  const handleSearch = async () => {
    try {
      setSearching(true);
      console.log('Search params:', searchParams);
      
      const results = await searchProperties(searchParams);
      console.log('Search results:', results);
      
      // Show results in alert for MVP
      if (results.length > 0) {
        alert(`Found ${results.length} properties matching your search!`);
      } else {
        alert('No properties found matching your criteria. Please try different filters.');
      }
    } catch (err) {
      console.error('Search error:', err);
      alert('Search failed. Please try again.');
    } finally {
      setSearching(false);
    }
  };

  return (
    <section
      id="home"
      className="relative min-h-screen flex items-center justify-center pt-20"
      style={{
        backgroundImage: 'url(https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/14u5wq92_ChatGPT%20Image%20Apr%2011%2C%202026%2C%2004_31_11%20PM.png)',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundAttachment: 'fixed'
      }}
    >
      {/* Overlay */}
      <div className="absolute inset-0 bg-gradient-to-r from-slate-900/90 via-slate-900/75 to-slate-900/60"></div>

      {/* Content */}
      <div className="relative z-10 container mx-auto px-4 py-20">
        <div className="max-w-4xl mx-auto text-center">
          {/* Headline */}
          <h1 className="text-5xl md:text-6xl lg:text-7xl font-bold text-white mb-6 leading-tight">
            Buy. Sell. Invest.
            <br />
            <span className="text-amber-500">With Confidence.</span>
          </h1>

          {/* Sub-heading */}
          <p className="text-xl md:text-2xl text-slate-200 mb-12 font-light">
            Trusted Real Estate Advisors in Gurugram
          </p>

          {/* Search Bar */}
          <div className="bg-white rounded-2xl shadow-2xl p-6 md:p-8">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
              {/* Location */}
              <div>
                <label className="block text-sm font-semibold text-slate-700 mb-2">
                  Location
                </label>
                <Select onValueChange={(value) => setSearchParams({ ...searchParams, location: value })}>
                  <SelectTrigger className="w-full h-12 border-slate-300">
                    <SelectValue placeholder="Select Sector" />
                  </SelectTrigger>
                  <SelectContent>
                    {gurugramSectors.map((sector) => (
                      <SelectItem key={sector} value={sector}>
                        {sector}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              {/* Property Type */}
              <div>
                <label className="block text-sm font-semibold text-slate-700 mb-2">
                  Property Type
                </label>
                <Select onValueChange={(value) => setSearchParams({ ...searchParams, property_type: value })}>
                  <SelectTrigger className="w-full h-12 border-slate-300">
                    <SelectValue placeholder="Select Type" />
                  </SelectTrigger>
                  <SelectContent>
                    {propertyTypes.map((type) => (
                      <SelectItem key={type} value={type}>
                        {type}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              {/* Budget */}
              <div>
                <label className="block text-sm font-semibold text-slate-700 mb-2">
                  Budget
                </label>
                <Select onValueChange={(value) => setSearchParams({ ...searchParams, budget: value })}>
                  <SelectTrigger className="w-full h-12 border-slate-300">
                    <SelectValue placeholder="Select Budget" />
                  </SelectTrigger>
                  <SelectContent>
                    {budgetRanges.map((range) => (
                      <SelectItem key={range} value={range}>
                        {range}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
            </div>

            {/* Search Button */}
            <Button
              onClick={handleSearch}
              disabled={searching}
              className="w-full h-14 bg-amber-600 hover:bg-amber-700 text-white text-lg font-semibold disabled:opacity-50"
            >
              <Search className="w-5 h-5 mr-2" />
              {searching ? 'Searching...' : 'Search Properties'}
            </Button>
          </div>

          {/* CTA */}
          <div className="mt-8 flex flex-wrap gap-4 justify-center">
            <a href="#contact">
              <Button
                size="lg"
                className="bg-white text-slate-900 hover:bg-slate-100 px-8 py-6 text-lg font-semibold"
              >
                Contact Now
              </Button>
            </a>
            <a href="https://wa.me/918742932997?text=Hello%20Housing%20Capital,%20I'm%20interested%20in%20a%20property%20in%20Gurugram.%20Please%20assist." target="_blank" rel="noopener noreferrer">
              <Button
                size="lg"
                variant="outline"
                className="border-2 border-white text-white hover:bg-white hover:text-slate-900 px-8 py-6 text-lg font-semibold"
              >
                Chat on WhatsApp
              </Button>
            </a>
          </div>
        </div>
      </div>
    </section>
  );
};
