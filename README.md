# Movie Recommender System

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-green.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/your-repo-name.svg)](https://github.com/yourusername/your-repo-name/issues)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/your-repo-name.svg)](https://github.com/yourusername/your-repo-name/stargazers)

---

## Overview

This project is a **Movie Recommender System** that leverages content-based filtering to suggest movies based on their metadata. By processing movie overviews, genres, keywords, cast, and crew data from the TMDB dataset, the system computes similarities between movies and recommends the most relevant options. The app is built with Streamlit, providing an intuitive interface to explore movie recommendations.

---

## Features

- **Content-Based Filtering:** Utilizes movie metadata to compute similarities.
- **Natural Language Processing:** Processes and transforms movie data (overview, genres, keywords, cast, crew) into unified tags.
- **Cosine Similarity:** Computes similarity scores between movies.
- **Dynamic Poster Fetching:** Retrieves movie posters via the TMDB API.
- **Streamlit Web Interface:** Easy-to-use UI for browsing and selecting movies.
- **Efficient Storage:** Uses chunking to manage large similarity matrices.

---

## Tech Stack

- **Programming Language:** Python 3.x
- **Libraries:** Pandas, NumPy, scikit-learn, Pickle, Requests, SnowballStemmer
- **Framework:** Streamlit
- **APIs:** [TMDB API](https://www.themoviedb.org/documentation/api)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/momina02/Movies-Recommendation-System.git
cd your-repo-name
```

### 2. Install Dependencies

Make sure you have Python 3.7 or later installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Prepare the Dataset

Download the TMDB dataset files (`tmdb_credits.csv` and `tmdb_movies.csv`) and place them in the root directory of the project.

### 4. TMDB API Key

Obtain an API key from [TMDB](https://www.themoviedb.org/documentation/api) and insert it into the `api_key` variable inside `app.py`.

---

## Usage

To launch the web application locally, run:

```bash
streamlit run app.py
```

A browser window should automatically open displaying the Movie Recommender System interface. Select a movie from the dropdown and click **Recommend** to see similar movies along with their posters.

---

## How It Works

1. **Data Preprocessing:**
   - **Merge Datasets:** Combines movie credits and details.
   - **Data Cleaning:** Removes duplicates and null values.
   - **Feature Extraction:** Extracts key fields (genres, keywords, cast, crew, overview) and converts them into a unified tag.
   - **Text Processing:** Applies stemming and lowercasing to normalize text.

2. **Similarity Computation:**
   - **Vectorization:** Converts movie tags into numerical vectors using `CountVectorizer`.
   - **Cosine Similarity:** Computes similarity between movies using cosine similarity.
   - **Chunking:** Splits the similarity matrix into manageable chunks for efficient loading.

3. **Recommendation Engine:**
   - Upon movie selection, the engine retrieves the top 5 similar movies.
   - Movie posters are fetched dynamically from the TMDB API.

---

## Contributing

Contributions, issues, and feature requests are welcome!

1. **Fork the repository**
2. **Create a new branch** for your feature or bug fix: `git checkout -b feature/YourFeature`
3. **Commit your changes:** `git commit -m 'Add some feature'`
4. **Push to the branch:** `git push origin feature/YourFeature`
5. **Open a pull request**

---

## Project Link

Project Link: https://github.com/momina02/Movies-Recommendation-System.git
