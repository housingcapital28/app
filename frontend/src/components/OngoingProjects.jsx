import React, { useState, useEffect } from 'react';
import { Card, CardContent } from './ui/card';
import { Badge } from './ui/badge';
import { Button } from './ui/button';
import { MapPin, Building2, ArrowRight } from 'lucide-react';
import { getProjects } from '../api/api';

export const OngoingProjects = () => {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const data = await getProjects();
        setProjects(data);
      } catch (err) {
        console.error('Error loading projects:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchProjects();
  }, []);

  const handleLearnMore = (project) => {
    console.log('Learn more about:', project.name);
    alert(`${project.name}\n${project.location}\n\n${project.description}\n\nUnits: ${project.units}\nStatus: ${project.status}`);
  };

  if (loading) {
    return (
      <section id="projects" className="py-20 bg-slate-50">
        <div className="container mx-auto px-4">
          <div className="text-center">
            <div className="animate-pulse">
              <div className="h-12 bg-slate-300 rounded w-96 mx-auto"></div>
            </div>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section id="projects" className="py-20 bg-slate-50">
      <div className="container mx-auto px-4">
        {/* Section Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-slate-900 mb-4">
            Ongoing Projects in Gurugram
          </h2>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            Premium residential projects offering high returns and luxury living
          </p>
        </div>

        {/* Projects Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {projects.map((project) => (
            <Card
              key={project.id}
              className="overflow-hidden hover:shadow-2xl transition-all duration-300 group border-slate-200"
            >
              {/* Image */}
              <div className="relative h-64 overflow-hidden">
                <img
                  src={project.image}
                  alt={project.name}
                  className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                />
                <div className="absolute top-4 right-4">
                  <Badge className="bg-amber-600 text-white px-3 py-1">
                    {project.status}
                  </Badge>
                </div>
              </div>

              {/* Content */}
              <CardContent className="p-6">
                {/* Title */}
                <h3 className="text-2xl font-bold text-slate-900 mb-3">
                  {project.name}
                </h3>

                {/* Location */}
                <div className="flex items-center text-slate-600 mb-3">
                  <MapPin className="w-4 h-4 mr-2 text-amber-600" />
                  <span>{project.location}</span>
                </div>

                {/* Units */}
                <div className="flex items-center text-slate-600 mb-4">
                  <Building2 className="w-4 h-4 mr-2 text-amber-600" />
                  <span>{project.units}</span>
                </div>

                {/* Description */}
                <p className="text-slate-600 mb-6 leading-relaxed">
                  {project.description}
                </p>

                {/* Button */}
                <Button
                  onClick={() => handleLearnMore(project)}
                  className="w-full bg-slate-900 hover:bg-amber-600 text-white group-hover:bg-amber-600 transition-colors duration-300"
                >
                  Learn More
                  <ArrowRight className="w-4 h-4 ml-2" />
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};
