import streamlit as st
import pickle
import pandas as pd
import requests
import os 
from dotenv import load_dotenv

load_dotenv()
TMDB_TOKEN = os.getenv("TMDB_READ_ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {TMDB_TOKEN}",
    "accept": "application/json"
}

movies_dict = pickle.load(open('movie_list_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
new_df = pd.DataFrame(movies_dict)

st.title("Movie Recommender System")
selected_movie_name = st.selectbox('Movie_List: ', new_df['title'].values)

def recommend(movie):
    index = new_df[new_df['title'] == movie].index[0]
    enumerated_list = list(enumerate(similarity[index]))
    distances = sorted(enumerated_list, reverse=True, key= lambda x: x[1])
    movie_list = []
    
    for i in distances[1:6]:
        movie_list.append(new_df['title'].loc[i[0]])
    return movie_list

if st.button('Recommend'):
    movie_list = recommend(selected_movie_name)
    for movie in movie_list:
        st.write(movie)