import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const sendMessage = async (message) => {
  try {
    const response = await axios.post(`${API_URL}/chat`, { query: message });
    return response.data.response;
  } catch (error) {
    console.error('Error sending message:', error);
    throw error;
  }
};