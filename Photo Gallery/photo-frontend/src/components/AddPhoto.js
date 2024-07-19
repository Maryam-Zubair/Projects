import React, { useState } from 'react';
import axios from 'axios';



const AddPhoto = ({ onPhotoAdded }) => {
  const [image, setImage] = useState(null);
  const [addedBy, setAddedBy] = useState('');
  const [peopleInPhoto, setPeopleInPhoto] = useState('');

  const handleImageChange = (e) => setImage(e.target.files[0]);

  const handleAddPhoto = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('image', image);
    formData.append('added_by', addedBy);
    formData.append('people_in_photo', peopleInPhoto);

    try {
      await axios.post(`http://localhost:8000/photos/add/`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      onPhotoAdded();
      setImage(null);
      setAddedBy('');
      setPeopleInPhoto('');
    } catch (error) {
      console.error('Error adding photo:', error);
    }
  };

  return (
    <form onSubmit={handleAddPhoto}>
      <input type="file" onChange={handleImageChange} required />
      <input
        type="text"
        placeholder="Your Name"
        value={addedBy}
        onChange={(e) => setAddedBy(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="People in Photo"
        value={peopleInPhoto}
        onChange={(e) => setPeopleInPhoto(e.target.value)}
        required
      />
      <button type="submit">Add Photo</button>
    </form>
  );
};

export default AddPhoto;
