
import pandas as pd
import joblib


import pickle
import streamlit as st
import requests

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown("Do Visit @: ")
with col2:
    st.markdown(
        "[Linkedin](https://www.linkedin.com/in/prabhat-kumar-prajapati/)")
with col3:
    st.markdown("[Github](https://github.com/PrabhatPrajapati)")
with col4:
    st.markdown("[leetcode](https://leetcode.com/prabhat1999/)")
with col5:
    st.markdown("[portfolio](https://prabhatprajapati.github.io/portfolio/)")

st.sidebar.title("Movie Recommender System")

st.sidebar.caption(
    'This type of recommendation systems, takes in a movie that a user currently likes as input. Then it analyzes the contents (storyline, genre, cast, director etc.) of the movie to find out other movies which have similar content. Then it ranks similar movies according to their similarity scores and recommends the most relevant movies to the user.')

st.sidebar.title("Dataset")
st.sidebar.caption('The following main data source was used for this project:')

st.sidebar.markdown("[Movie dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)")

st.sidebar.title("Data Pre-processing")
st.sidebar.caption('''
* Dropping columns that are not required
* Merging dataframes''')

st.sidebar.title("Cosine Similarity")
st.sidebar.caption('''
Also known as vector-based similarity, this formulation views two items and their ratings as vectors, and defines the similarity between them as the angle between these vectors:''')


st.sidebar.title("Recommender")
st.sidebar.caption('''
* User enters his favourite movie (or the movie on the basis of which he wants the system to recommend movies)
* Based on the user's input, recommendation is made by sorting the similarities in descending order''')


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pd.read_csv("file1.csv")
similarity = joblib.load("similarity.pkl")

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])


import webbrowser

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: visible;}
            footer:after{
                background-color:#728FCE;
                font-size:12px;
                font-weight:5px;
                height:30px;
                margin:1rem;
                padding:0.8rem;
                content:'Copyright © 2022 : Prabhat Kumar';
                display: flex;
                align-items:center;
                justify-content:center;
                color:white;
            }
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



