import React from 'react';
import { Button } from './ui/button';
import { MapPin, Phone, Mail, Facebook, Instagram, Linkedin, Youtube } from 'lucide-react';
import { Separator } from './ui/separator';

export const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer id="contact" className="bg-slate-900 text-slate-300">
      {/* Main Footer */}
      <div className="container mx-auto px-4 py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12">
          {/* Company Info */}
          <div>
            <h3 className="text-2xl font-bold text-white mb-4">Housing Capital</h3>
            <p className="text-sm text-amber-500 mb-4">Construction & Real Estate</p>
            <p className="text-slate-400 leading-relaxed mb-6">
              Your trusted partner for premium builder floors, apartments, plots, and investment properties in Gurugram.
            </p>
            <a
              href="https://wa.me/918742932997?text=Hello%20Housing%20Capital,%20I'm%20interested%20in%20a%20property%20in%20Gurugram.%20Please%20assist."
              target="_blank"
              rel="noopener noreferrer"
            >
              <Button className="bg-amber-600 hover:bg-amber-700 text-white">
                WhatsApp Us
              </Button>
            </a>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-lg font-bold text-white mb-4">Quick Links</h4>
            <ul className="space-y-3">
              <li>
                <a href="#home" className="hover:text-amber-500 transition-colors duration-200">
                  Home
                </a>
              </li>
              <li>
                <a href="#properties" className="hover:text-amber-500 transition-colors duration-200">
                  Buy Property
                </a>
              </li>
              <li>
                <a href="#sell" className="hover:text-amber-500 transition-colors duration-200">
                  Sell Property
                </a>
              </li>
              <li>
                <a href="#projects" className="hover:text-amber-500 transition-colors duration-200">
                  Projects
                </a>
              </li>
              <li>
                <a href="#investment" className="hover:text-amber-500 transition-colors duration-200">
                  Investment Deals
                </a>
              </li>
            </ul>
          </div>

          {/* Property Types */}
          <div>
            <h4 className="text-lg font-bold text-white mb-4">Property Types</h4>
            <ul className="space-y-3">
              <li>
                <a href="#properties" className="hover:text-amber-500 transition-colors duration-200">
                  Builder Floors
                </a>
              </li>
              <li>
                <a href="#properties" className="hover:text-amber-500 transition-colors duration-200">
                  Luxury Apartments
                </a>
              </li>
              <li>
                <a href="#properties" className="hover:text-amber-500 transition-colors duration-200">
                  Premium Plots
                </a>
              </li>
              <li>
                <a href="#properties" className="hover:text-amber-500 transition-colors duration-200">
                  Commercial Spaces
                </a>
              </li>
              <li>
                <a href="#properties" className="hover:text-amber-500 transition-colors duration-200">
                  Investment Properties
                </a>
              </li>
            </ul>
          </div>

          {/* Contact Info */}
          <div>
            <h4 className="text-lg font-bold text-white mb-4">Contact Us</h4>
            <ul className="space-y-4">
              <li className="flex items-start">
                <MapPin className="w-5 h-5 text-amber-500 mr-3 mt-1 flex-shrink-0" />
                <span>Gurugram, Haryana, India</span>
              </li>
              <li className="flex items-center">
                <Phone className="w-5 h-5 text-amber-500 mr-3 flex-shrink-0" />
                <a href="tel:+918742932997" className="hover:text-amber-500 transition-colors duration-200">
                  87429 32997
                </a>
              </li>
              <li className="flex items-center">
                <Mail className="w-5 h-5 text-amber-500 mr-3 flex-shrink-0" />
                <a href="mailto:info@housingcapital.in" className="hover:text-amber-500 transition-colors duration-200">
                  info@housingcapital.in
                </a>
              </li>
            </ul>

            {/* Social Media */}
            <div className="mt-6">
              <h5 className="text-sm font-semibold text-white mb-3">Follow Us</h5>
              <div className="flex gap-3">
                <a
                  href="#"
                  className="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-amber-600 transition-colors duration-300"
                >
                  <Facebook className="w-5 h-5" />
                </a>
                <a
                  href="#"
                  className="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-amber-600 transition-colors duration-300"
                >
                  <Instagram className="w-5 h-5" />
                </a>
                <a
                  href="#"
                  className="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-amber-600 transition-colors duration-300"
                >
                  <Linkedin className="w-5 h-5" />
                </a>
                <a
                  href="#"
                  className="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-amber-600 transition-colors duration-300"
                >
                  <Youtube className="w-5 h-5" />
                </a>
              </div>
            </div>
          </div>

          {/* Logo Column - Right Side */}
          <div className="flex items-center justify-center lg:justify-end">
            <img
              src="https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/qmee7kc2_ChatGPT%20Image%20Apr%2011%2C%202026%2C%2003_26_00%20PM.png"
              alt="Housing Capital Logo"
              className="h-56 md:h-64 lg:h-72 w-auto object-contain opacity-90 hover:opacity-100 transition-opacity duration-300"
              style={{ filter: 'brightness(0) invert(1)' }}
            />
          </div>
        </div>
      </div>

      <Separator className="bg-slate-800" />

      {/* Bottom Footer */}
      <div className="container mx-auto px-4 py-6">
        <div className="text-center text-sm text-slate-400">
          <p>© {currentYear} Housing Capital Construction & Real Estate. All rights reserved.</p>
          <p className="mt-2">Trusted Real Estate Advisors in Gurugram</p>
        </div>
      </div>
    </footer>
  );
};
