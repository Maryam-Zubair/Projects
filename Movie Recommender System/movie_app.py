from flask import Flask, render_template, request
from fuzzywuzzy import fuzz
import pandas as pd
import numpy as np
import ast

app = Flask(__name__)

# genres, overview, spoken_languages
movie = pd.read_csv('tmdb_5000_movies.csv')
# movie_id , title , cast , crew
credit = pd.read_csv('tmdb_5000_credits.csv')
#merging two datasets
data = movie.merge(credit, on='title')
# filtering the required data
data = data[['genres','overview','spoken_languages','movie_id','title','cast','crew']]

# PRE-PROCESSING THE DATA 
# 1. checking null values
x = data.isnull().sum()

# 2. dropping null values
data.dropna(inplace=True)
y = data.isnull().sum()

# 3. checking duplicates
data.duplicated().sum()

# as in genre we just need type of genre not other details
def convert(obj):
    return_list1=[]
    # ast.literal_eval string into a list
    for i in ast.literal_eval(obj):
        return_list1.append(i['name'])
    return return_list1

data['genres'] = data['genres'].apply(convert)
data['spoken_languages'] = data['spoken_languages'].apply(convert)

# 5 people in the cast
def char(obj):
    return_list2 =[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter <5:
            return_list2.append(i['name'])
            counter = counter + 1
        else:
            break
    return return_list2

data['cast'] = data['cast'].apply(char)

# director name
def dir_name(obj):
    name=[]
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            name.append(i['name'])
            break
    return name
data['crew'] = data['crew'].apply(dir_name)


# MAIN WORKING FOR CONTENT BASED RECOMMENDATION SYSTEM
# 1. Feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer

# converting string into list befire concatenation:
data['genres'] = data['genres'].apply(lambda x: ' '.join(x))
data['spoken_languages'] = data['spoken_languages'].apply(lambda x: ' '.join(x))
data['cast'] = data['cast'].apply(lambda x: ' '.join(x))
data['crew'] = data['crew'].apply(lambda x: ' '.join(x) if x else '') 

# Concatenating features into a single string
data['tag'] = data['overview'] + " " + data['genres'] + " " + data['spoken_languages'] + " " + data['cast'] + " " + data['crew']

# 2. Vectorization
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = tfidf.fit_transform(data['tag'])

# 3. Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)

# 4. Building Recommendation Function

def recommendation(title):
    matching_titles = [t for t in data['title'] if fuzz.ratio(title, t) >= 80]

    if not matching_titles:
        return ["Movie not found"]

    # if title not in data['title'].values:
    #     return ["Movie not found"]
    title = matching_titles[0]
    index = data[data['title'] == title].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append((data.iloc[i[0]].title, data.iloc[i[0]].overview))
    return recommended_movies


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        movie_name = request.form["movie"]
        recommendations = recommendation(movie_name)
        return render_template("index.html", recommendations=recommendations)
    return render_template("index.html", recommendations=[])

if __name__ == "__main__":
    app.run(debug=True)


