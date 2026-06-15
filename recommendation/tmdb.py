import requests
import pandas as pd
from config import TMDB_API_KEY

# Cache
movie_cache = {}

# Load links dataset once
links = pd.read_csv("dataset/links.csv")


def get_movie_details(movie_id):

    try:

        movie_id = int(movie_id)

        # Cache Check
        if movie_id in movie_cache:
            return movie_cache[movie_id]

        movie_row = links[
            links["movieId"] == movie_id
        ]

        if movie_row.empty:
            return None

        tmdb_id = int(
            movie_row.iloc[0]["tmdbId"]
        )

        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{tmdb_id}",
            params={
                "api_key": TMDB_API_KEY,
                "append_to_response": "credits,videos"
            },
            timeout=5
        )

        if response.status_code != 200:
            return None

        movie = response.json()

        # Poster
        poster = ""

        if movie.get("poster_path"):

            poster = (
                "https://image.tmdb.org/t/p/w500"
                + movie["poster_path"]
            )

        # Genres
        genres = ", ".join(
            [
                genre["name"]
                for genre in movie.get(
                    "genres",
                    []
                )
            ]
        )

        # Runtime
        runtime = movie.get(
            "runtime",
            0
        )

        # Overview
        overview = movie.get(
            "overview",
            "No overview available."
        )

        # IMDb
        imdb_id = movie.get(
            "imdb_id",
            ""
        )

        imdb_link = ""

        if imdb_id:

            imdb_link = (
                f"https://www.imdb.com/title/{imdb_id}"
            )

        # Cast
        cast_names = []

        for actor in movie.get(
            "credits",
            {}
        ).get(
            "cast",
            []
        )[:5]:

            cast_names.append(
                actor.get("name")
            )

        cast = ", ".join(
            cast_names
        )

        # Trailer
        trailer_url = ""

        for video in movie.get(
            "videos",
            {}
        ).get(
            "results",
            []
        ):

            if (
                video.get("site") == "YouTube"
                and video.get("type") == "Trailer"
            ):

                trailer_url = (
                    "https://www.youtube.com/watch?v="
                    + video["key"]
                )

                break

        movie_data = {

            "title": movie.get(
                "title",
                "Unknown"
            ),

            "rating": round(
                movie.get(
                    "vote_average",
                    0
                ),
                1
            ),

            "release_date": movie.get(
                "release_date",
                "N/A"
            ),

            "poster": poster,

            "overview": overview,

            "genres": genres,

            "runtime": runtime,

            "cast": cast,

            "imdb_link": imdb_link,

            "trailer": trailer_url
        }

        # Save To Cache
        movie_cache[movie_id] = movie_data

        return movie_data

    except Exception as e:

        print(
            "TMDB ERROR:",
            e
        )

        return None