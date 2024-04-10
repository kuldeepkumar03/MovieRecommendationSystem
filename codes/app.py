import streamlit as st
import pickle
import pandas as pd

def recommendation(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = sim[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:8]
    
    recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
    
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

sim = pickle.load(open('sim.pkl','rb'))

st.title("Recommendation System")

selected_movie_name = st.selectbox(
    "Please Select The Movies.",
    movies['title'].values 
)

if st.button("Recommend"):
    recommendations = recommendation(selected_movie_name)
    for i in recommendations:
        st.write(i)
