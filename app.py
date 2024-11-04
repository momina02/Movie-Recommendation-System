# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# import math

# def fetch_poster(movie_id):
#     api_key = st.secrets["TMBDA_API_KEY"]
#     response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}")
#     data = response.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def load_similarity_chunk(movie_index, num_chunks=20):
#     chunk_size = math.ceil(len(movies) / num_chunks)
#     chunk_index = movie_index // chunk_size
#     with open(f'similarity_chunk_{chunk_index}.pkl', 'rb') as f:
#         similarity_chunk = pickle.load(f)
#     return similarity_chunk[movie_index % chunk_size]

# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = load_similarity_chunk(movie_index)
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters

# # Load the movie data from the pickle file
# with open('movie_dict.pkl', 'rb') as file:
#     movie_dict = pickle.load(file)

# # Convert the dictionary to a DataFrame
# movies = pd.DataFrame(movie_dict)

# st.title("Movie Recommender System")

# text = st.markdown("<h3 style='text-align: left;'>Select a movie that you would like to watch</h3>", unsafe_allow_html=True)
# selected_movie_name = st.selectbox(
#     # 'What would you like to watch?',
#     '',
#     movies['title'].values,
# )


# if st.button('Recommend'):
#     st.write('')
#     st.write('')
#     names, posters = recommend(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)

#     with col1:
#         st.markdown(f"<div style='height: 110px; overflow: hidden; text-align: left; font-size:17px;'>{names[0]}</div>", unsafe_allow_html=True)
#         st.image(posters[0], use_column_width=True)
#     with col2:
#         st.markdown(f"<div style='height: 110px; overflow: hidden; text-align: left; font-size:17px;'>{names[1]}</div>", unsafe_allow_html=True)
#         st.image(posters[1], use_column_width=True)
#     with col3:
#         st.markdown(f"<div style='height: 110px; overflow: hidden; text-align: left; font-size:17px;'>{names[2]}</div>", unsafe_allow_html=True)
#         st.image(posters[2], use_column_width=True)
#     with col4:
#         st.markdown(f"<div style='height: 110px; overflow: hidden; text-align: left; font-size:17px;'>{names[3]}</div>", unsafe_allow_html=True)
#         st.image(posters[3], use_column_width=True)
#     with col5:
#         st.markdown(f"<div style='height: 110px; overflow: hidden; text-align: left; font-size:17px;'>{names[4]}</div>", unsafe_allow_html=True)
#         st.image(posters[4], use_column_width=True)


import streamlit as st
import pickle
import pandas as pd
import requests
import math
import os

def fetch_poster(movie_id):
    api_key = st.secrets["TMBDA_API_KEY"]
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}")
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def create_similarity_chunks(similarity_matrix, num_chunks=20):
    """Splits the full similarity matrix into smaller chunks and saves them as separate .pkl files."""
    chunk_size = math.ceil(len(similarity_matrix) / num_chunks)
    for i in range(num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, len(similarity_matrix))
        chunk = similarity_matrix[start:end]
        with open(f'similarity_chunk_{i}.pkl', 'wb') as f:
            pickle.dump(chunk, f)
    print(f"Created {num_chunks} similarity chunks.")

def load_similarity_chunk(movie_index, num_chunks=20):
    chunk_size = math.ceil(len(movies) / num_chunks)
    chunk_index = movie_index // chunk_size
    with open(f'similarity_chunk_{chunk_index}.pkl', 'rb') as f:
        similarity_chunk = pickle.load(f)
    return similarity_chunk[movie_index % chunk_size]

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = load_similarity_chunk(movie_index)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load the movie data from the pickle file
with open('movie_dict.pkl', 'rb') as file:
    movie_dict = pickle.load(file)

# Convert the dictionary to a DataFrame
movies = pd.DataFrame(movie_dict)

# Load or create similarity chunks
if not all(os.path.exists(f'similarity_chunk_{i}.pkl') for i in range(20)):
    # Load your full similarity matrix (if you have it saved somewhere)
    with open('similarity.pkl', 'rb') as f:
        full_similarity_matrix = pickle.load(f)
    create_similarity_chunks(full_similarity_matrix)

st.title("Movie Recommender System")

text = st.markdown("<h3 style='text-align: left;'>Select a movie that you would like to watch</h3>", unsafe_allow_html=True)
selected_movie_name = st.selectbox(
    # 'What would you like to watch?',
    '',
    movies['title'].values,
)

if st.button('Recommend'):
    st.write('')
    st.write('')
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f"<div style='height: 110px; overflow: hidden; text-align: left; font-size:17px;'>{names[0]}</div>", unsafe_allow_html=True)
        st.image(posters[0], use_column_width=True)
    with col2:
        st.markdown(f"<div style='height: 110px; overflow: hidden; text-align: left; font-size:17px;'>{names[1]}</div>", unsafe_allow_html=True)
        st.image(posters[1], use_column_width=True)
    with col3:
        st.markdown(f"<div style='height: 110px; overflow: hidden; text-align: left; font-size:17px;'>{names[2]}</div>", unsafe_allow_html=True)
        st.image(posters[2], use_column_width=True)
    with col4:
        st.markdown(f"<div style='height: 110px; overflow: hidden; text-align: left; font-size:17px;'>{names[3]}</div>", unsafe_allow_html=True)
        st.image(posters[3], use_column_width=True)
    with col5:
        st.markdown(f"<div style='height: 110px; overflow: hidden; text-align: left; font-size:17px;'>{names[4]}</div>", unsafe_allow_html=True)
        st.image(posters[4], use_column_width=True)
