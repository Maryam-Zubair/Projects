import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AddPhoto from './components/AddPhoto';
import PhotoList from './components/ViewPhoto';
import ImageGallery from './components/ImageGallery';
import './App.css';

const App = () => {
  return (
    <Router>
      <div className="App">
        <h1>Photo Gallery </h1>
        <Routes>
          <Route path="/" element={
            <>
              <AddPhoto />
              <PhotoList />
            </>
          } />
          <Route path="/gallery" element={<ImageGallery />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;