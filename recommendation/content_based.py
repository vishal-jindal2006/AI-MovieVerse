import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("dataset/movies.csv")

# Fill missing values
movies["genres"] = movies["genres"].fillna("")

# Convert genres into vectors
tfidf = TfidfVectorizer(
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(
    movies["genres"]
)

# Similarity Matrix
similarity = cosine_similarity(
    tfidf_matrix
)


def recommend(movie_name, top_n=5):

    movie_name = movie_name.lower()

    matches = movies[
        movies["title"].str.lower().str.contains(
            movie_name,
            na=False
        )
    ]

    if matches.empty:
        return []

    movie_index = matches.index[0]

    distances = list(
        enumerate(
            similarity[movie_index]
        )
    )

    distances = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for movie in distances[1:top_n + 1]:

        movie_data = movies.iloc[
            movie[0]
        ]

        recommendations.append({
            "movieId": int(
                movie_data["movieId"]
            ),
            "title": movie_data["title"]
        })

    return recommendations