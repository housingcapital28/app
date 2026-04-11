import React, { useState, useEffect } from 'react';
import { Button } from './ui/button';
import { Phone, Menu, X } from 'lucide-react';

export const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const menuItems = [
    { label: 'Home', href: '#home' },
    { label: 'Buy Property', href: '#properties' },
    { label: 'Sell Property', href: '#sell' },
    { label: 'Projects', href: '#projects' },
    { label: 'Investment Deals', href: '#investment' },
    { label: 'About Us', href: '#about' },
    { label: 'Contact', href: '#contact' }
  ];

  const handleNavClick = (e, href) => {
    e.preventDefault();
    setIsMobileMenuOpen(false);
    const element = document.querySelector(href);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        isScrolled ? 'bg-white shadow-md py-3' : 'bg-white/95 backdrop-blur-sm py-4'
      }`}
    >
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between">
          {/* Logo */}
          <div className="flex items-center bg-black px-3 py-2 rounded-lg">
            <img
              src="https://customer-assets.emergentagent.com/job_gurugram-luxury/artifacts/puln9hgq_ChatGPT%20Image%20Apr%2011%2C%202026%2C%2003_26_00%20PM.png"
              alt="Housing Capital Logo"
              className="h-16 md:h-20 w-auto object-contain"
            />
          </div>

          {/* Desktop Menu */}
          <div className="hidden lg:flex items-center space-x-8">
            {menuItems.map((item) => (
              <a
                key={item.label}
                href={item.href}
                onClick={(e) => handleNavClick(e, item.href)}
                className="text-slate-700 hover:text-amber-600 font-medium text-sm transition-colors duration-200"
              >
                {item.label}
              </a>
            ))}
          </div>

          {/* Contact Button */}
          <div className="hidden lg:flex items-center space-x-3">
            <a href="tel:+918742932997">
              <Button className="bg-amber-600 hover:bg-amber-700 text-white">
                <Phone className="w-4 h-4 mr-2" />
                87429 32997
              </Button>
            </a>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            className="lg:hidden text-slate-900 p-2"
          >
            {isMobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {/* Mobile Menu */}
        {isMobileMenuOpen && (
          <div className="lg:hidden mt-4 pb-4 border-t border-slate-200 pt-4">
            <div className="flex flex-col space-y-3">
              {menuItems.map((item) => (
                <a
                  key={item.label}
                  href={item.href}
                  onClick={(e) => handleNavClick(e, item.href)}
                  className="text-slate-700 hover:text-amber-600 font-medium text-sm py-2"
                >
                  {item.label}
                </a>
              ))}
              <a href="tel:+918742932997" className="pt-2">
                <Button className="w-full bg-amber-600 hover:bg-amber-700 text-white">
                  <Phone className="w-4 h-4 mr-2" />
                  87429 32997
                </Button>
              </a>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};
