import React from 'react';
import { Navbar } from '../components/Navbar';
import { HeroSection } from '../components/HeroSection';
import { FeaturedProperties } from '../components/FeaturedProperties';
import { WhyChooseUs } from '../components/WhyChooseUs';
import { OngoingProjects } from '../components/OngoingProjects';
import { Testimonials } from '../components/Testimonials';
import { CTASection } from '../components/CTASection';
import { Footer } from '../components/Footer';

export const HomePage = () => {
  return (
    <div className="min-h-screen">
      <Navbar />
      <HeroSection />
      <FeaturedProperties />
      <WhyChooseUs />
      <OngoingProjects />
      <Testimonials />
      <CTASection />
      <Footer />
    </div>
  );
};
