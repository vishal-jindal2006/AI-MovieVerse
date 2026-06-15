from recommendation.content_based import recommend
from recommendation.collaborative import collaborative_recommend


def hybrid_recommend(movie_name):

    content_movies = recommend(
        movie_name,
        top_n=15
    )

    collaborative_movies = collaborative_recommend(
        movie_name,
        top_n=15
    )

    final_movies = []

    seen_ids = set()

    for movie in content_movies:

        if movie["movieId"] not in seen_ids:

            final_movies.append(movie)

            seen_ids.add(
                movie["movieId"]
            )

    for movie in collaborative_movies:

        if movie["movieId"] not in seen_ids:

            final_movies.append(movie)

            seen_ids.add(
                movie["movieId"]
            )

    return final_movies[:20]