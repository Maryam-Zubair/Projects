import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';


const API_BASE_URL = 'http://3.84.1.254:8000';

const ImageGallery = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const photos = location.state?.photos || [];

  return (
    <div>
      <h2>Image Gallery</h2>
      <button onClick={() => navigate('/')}>Back to Search</button>
      <ul>
        {photos.map((photo) => (
          <li key={photo.id}>
            <img src={`${API_BASE_URL}${photo.image}`} alt="Family" />
            <p>Added by: {photo.added_by}</p>
            <p>People in Photo: {photo.people_in_photo}</p>
            <p>Date: {new Date(photo.date_added).toLocaleDateString()}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ImageGallery;
