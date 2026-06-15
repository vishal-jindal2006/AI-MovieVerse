import pandas as pd

ratings = pd.read_csv("dataset/ratings.csv")
movies = pd.read_csv("dataset/movies.csv")


def collaborative_recommend(movie_name, top_n=5):

    movie_match = movies[
        movies["title"].str.lower().str.contains(
            movie_name.lower(),
            na=False
        )
    ]

    if movie_match.empty:
        return []

    movie_id = movie_match.iloc[0]["movieId"]

    users_who_liked = ratings[
        (ratings["movieId"] == movie_id)
        & (ratings["rating"] >= 4)
    ]["userId"]

    similar_movies = ratings[
        (ratings["userId"].isin(users_who_liked))
        & (ratings["rating"] >= 4)
    ]

    recommendation_scores = (
        similar_movies["movieId"]
        .value_counts()
        .reset_index()
    )

    recommendation_scores.columns = [
        "movieId",
        "score"
    ]

    recommendation_scores = recommendation_scores[
        recommendation_scores["movieId"] != movie_id
    ]

    recommendation_scores = recommendation_scores.head(top_n)

    recommendations = []

    for _, row in recommendation_scores.iterrows():

        movie = movies[
            movies["movieId"] == row["movieId"]
        ]

        if not movie.empty:

            recommendations.append({
                "movieId": int(
                    movie.iloc[0]["movieId"]
                ),
                "title": movie.iloc[0]["title"]
            })

    return recommendations