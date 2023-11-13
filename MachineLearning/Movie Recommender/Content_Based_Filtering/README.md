
# Movie Recommender System

## Overview
This movie recommender system is a content-based filtering application that suggests movies based on the similarity of their content. It utilizes a dataset from TMDB (The Movie Database) and recommends movies considering features such as genres, overviews, spoken languages, cast, and crew details. Built with Python and Flask, this project offers a user-friendly web interface for easy interaction.

## Features
- Content-Based Filtering: Utilizes movie content for recommendations.
- Flask Web Application: Provides a simple and interactive user interface.
- TMDB 5000 Movie Dataset: Employs a comprehensive movie dataset.

## Installation and Setup

### Clone the Repository
git clone 

### Istall Dependencies
Ensure Python is installed on your system.
Install required Python packages:

```bash
pip install flask pandas scikit-learn
```

### Data Preparation
Download the TMDB 5000 Movie Dataset.
Place tmdb_5000_movies.csv and tmdb_5000_credits.csv in the project directory.
### Running the Application
Start the Flask server:
```bash
python app.py
```
Access the web application at http://127.0.0.1:5000/.

## Usage

Access the Web Interface:
Open your browser and go to http://127.0.0.1:5000/.

Movie Recommendation:
Enter the name of a movie you like in the search box and click "Recommend".

View Recommendations:
The system will display a list of recommended movies based on content similarity.

## Technologies Used

Python: Primary programming language for the recommender algorithm.

Flask: Web framework for creating the web interface.

Pandas: Data manipulation and analysis.

Scikit-Learn: Machine learning library for vectorization and similarity calculation.

