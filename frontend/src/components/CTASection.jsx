import React from 'react';
import { Button } from './ui/button';
import { Phone, MessageCircle } from 'lucide-react';

export const CTASection = () => {
  return (
    <section id="investment" className="py-20 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 relative overflow-hidden">
      {/* Decorative Elements */}
      <div className="absolute inset-0 opacity-10">
        <div className="absolute top-0 left-0 w-96 h-96 bg-amber-600 rounded-full blur-3xl"></div>
        <div className="absolute bottom-0 right-0 w-96 h-96 bg-amber-600 rounded-full blur-3xl"></div>
      </div>

      <div className="container mx-auto px-4 relative z-10">
        <div className="max-w-4xl mx-auto text-center">
          {/* Heading */}
          <h2 className="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-6">
            Looking to Buy, Sell or Rent in Gurugram?
          </h2>

          {/* Subheading */}
          <p className="text-xl md:text-2xl text-slate-300 mb-10">
            Connect with our expert advisors for personalized assistance
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="tel:+918742932997">
              <Button
                size="lg"
                className="bg-amber-600 hover:bg-amber-700 text-white px-10 py-7 text-lg font-semibold shadow-xl hover:shadow-2xl transition-all duration-300"
              >
                <Phone className="w-5 h-5 mr-2" />
                Call Now
              </Button>
            </a>

            <a
              href="https://wa.me/918742932997?text=Hello%20Housing%20Capital,%20I'm%20interested%20in%20a%20property%20in%20Gurugram.%20Please%20assist."
              target="_blank"
              rel="noopener noreferrer"
            >
              <Button
                size="lg"
                variant="outline"
                className="border-2 border-white text-white hover:bg-white hover:text-slate-900 px-10 py-7 text-lg font-semibold shadow-xl hover:shadow-2xl transition-all duration-300"
              >
                <MessageCircle className="w-5 h-5 mr-2" />
                Chat on WhatsApp
              </Button>
            </a>
          </div>

          {/* Contact Info */}
          <div className="mt-10 text-slate-300">
            <p className="text-lg">📞 87429 32997</p>
            <p className="text-sm mt-2">Available 7 days a week • 9 AM - 9 PM</p>
          </div>
        </div>
      </div>
    </section>
  );
};
