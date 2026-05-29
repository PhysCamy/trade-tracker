import axios from 'axios';

// Create an instance of Axios with the base url
const api = axios.create({
    baseURL: "http://localhost:8000"
});

// Export the Axios instance
export default api;