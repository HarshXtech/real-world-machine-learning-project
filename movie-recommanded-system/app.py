import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{0}?api_key=9f55a828bb597643d16ff71427de2b7e&language=en-US'.format(movie_id))

    data = response.json()

    # print(data)
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']



main_movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))
def recommand(movie):
    movie_index = main_movies_list[main_movies_list['title'] == movie].index[0]
    distances = similarity_matrix[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x : x[1])[1:6]
    

    recommanded_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = main_movies_list.iloc[i[0]].movie_id
        recommanded_movies.append(main_movies_list.iloc[i[0]]['title'])
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommanded_movies, recommended_movies_poster
    
movies_list = main_movies_list['title'].values



st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Hey! What would you like to open?', 
    (movies_list)
)

if st.button('Search'):
    name, poster = recommand(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(name[0])
        st.image(poster[0])
    with col2:
        st.header(name[1])
        st.image(poster[1])
    with col3:
        st.header(name[2])
        st.image(poster[2])
    with col4:
        st.header(name[3])
        st.image(poster[3])
    with col5:
        st.header(name[4])
        st.image(poster[4])