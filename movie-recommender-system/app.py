import streamlit as st
import pandas as pd
import pickle
import requests
def fetch_poster(movie_title):
    api_key = '2a28b305'  # Replace with your actual API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    try:
        data = requests.get(url).json()
        # Returns the poster URL if found, else a default placeholder
        return data.get('Poster', "https://via.placeholder.com/500x750?text=No+Poster+Found")
    except:
        return "https://via.placeholder.com/500x750?text=Error"
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    r=[]
    rp=[]
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        r.append(movie_title)
        rp.append(fetch_poster(movie_title))
    return r,rp
st.title('Movie Recommender System')
movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
option = st.selectbox(
    "Enter Movie Name",
    movies['title'].values,
)
if st.button("Recommend"):
    recommendation,poster=recommend(option)
    col1, col2, col3, col4,col5 = st.columns(5)

    with col1:
        st.text(recommendation[0])
        st.image(poster[0])

    with col2:
        st.text(recommendation[1])
        st.image(poster[1])

    with col3:
        st.text(recommendation[2])
        st.image(poster[2])
    with col4:
        st.text(recommendation[3])
        st.image(poster[3])
    with col5:
        st.text(recommendation[4])
        st.image(poster[4])