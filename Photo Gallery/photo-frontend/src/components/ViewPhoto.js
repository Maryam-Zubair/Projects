import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const PhotoList = () => {
  const [searchName, setSearchName] = useState('');
  const [searchDate, setSearchDate] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const fetchPhotos = async () => {
    try {
      setError(null);
      const response = await axios.get('http://localhost:8000/photos/view/', {
        params: { name: searchName, date: searchDate },
      });
      navigate('/gallery', { state: { photos: response.data } });
    } catch (error) {
      console.error('Error fetching photos:', error);
      setError('Failed to fetch photos. Please try again later.');
    }
  };

  return (
    <div>
      <h2>Search Photos</h2>
      <div className="search-container">
        <input
          type="text"
          placeholder="Search by Name"
          value={searchName}
          onChange={(e) => setSearchName(e.target.value)}
        />
        <input
          type="date"
          placeholder="Search by Date"
          value={searchDate}
          onChange={(e) => setSearchDate(e.target.value)}
        />
        <button onClick={fetchPhotos}>Search</button>
      </div>
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

export default PhotoList;
