# movies_recommendation_system
This repository contains the code for building movie recommendation engine.
# Collaborative Filterin
- Collaborative Filtering simply put uses the "wisdom of the crowd" to recommend items.
- Item based collaborative filtering uses the patterns of users who liked the same movie as me to recommend me a movie (users who liked the movie that I like, also liked these other movies).
- Recommendation based on user's input of any movie present in the dataset.
# Files
- Movie_Recommender_Notebook.ipynb: Jupyter notebook with step-by-step instructions
- Movie_Recommender_User_Input.py: Python file for allowing user's input of movie
# Dataset
The following main data source was used for this project:
- [Movie dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)
# Data Pre-processing
- Dropping columns that are not required
- Merging dataframes
# Cosine Similarity
- Also known as vector-based similarity, this formulation views two items and their ratings as vectors, and defines the similarity between them as the angle between these vectors:
- ![image](https://user-images.githubusercontent.com/96784632/183915924-974d6e7e-124f-46af-bcfe-5150f9eb1d0b.png)


# Recommender
- User enters his favourite movie (or the movie on the basis of which he wants the system to recommend movies)
- Based on the user's input, recommendation is made by sorting the similarities in descending order
