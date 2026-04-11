import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

// Property API calls
export const getProperties = async () => {
  try {
    const response = await axios.get(`${API}/properties`);
    return response.data;
  } catch (error) {
    console.error('Error fetching properties:', error);
    throw error;
  }
};

export const getProperty = async (id) => {
  try {
    const response = await axios.get(`${API}/properties/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching property:', error);
    throw error;
  }
};

export const searchProperties = async (searchParams) => {
  try {
    const response = await axios.post(`${API}/properties/search`, searchParams);
    return response.data;
  } catch (error) {
    console.error('Error searching properties:', error);
    throw error;
  }
};

// Project API calls
export const getProjects = async () => {
  try {
    const response = await axios.get(`${API}/projects`);
    return response.data;
  } catch (error) {
    console.error('Error fetching projects:', error);
    throw error;
  }
};

// Lead API calls
export const submitLead = async (leadData) => {
  try {
    const response = await axios.post(`${API}/leads`, leadData);
    return response.data;
  } catch (error) {
    console.error('Error submitting lead:', error);
    throw error;
  }
};

// Testimonial API calls
export const getTestimonials = async () => {
  try {
    const response = await axios.get(`${API}/testimonials`);
    return response.data;
  } catch (error) {
    console.error('Error fetching testimonials:', error);
    throw error;
  }
};
