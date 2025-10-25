import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get(('https://api.themoviedb.org/3/movie/{}?api_key=4a43ca6a5fba704b1335dd7b57c4976a'.format(movie_id)))
    data = response.json()
    return f'https://image.tmdb.org/t/p/w500' + data['poster_path']

def recommended(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_poster = []
    recommend = []
    for i in movies_list:
        movie_id = movies_df.iloc[i[0]].id
        recommend.append(movies_df.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))
    return recommend,recommended_poster

movie_pkl = pickle.load(open('movies_dict.pkl','rb'))
movies_df = pd.DataFrame(movie_pkl)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender system')
selected_movie_name = st.selectbox('select movie',(movies_df['title'].values))

if st.button('Recommend'):
    names,posters = recommended(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])