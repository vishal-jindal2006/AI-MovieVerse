from flask import Flask, render_template, request

from recommendation.hybrid import hybrid_recommend
from recommendation.tmdb import get_movie_details
from recommendation.content_based import movies

from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    movie_name = ""
    no_results = False

    movie_titles = movies["title"].tolist()

    if request.method == "POST":

        movie_name = request.form.get(
            "movie",
            ""
        ).strip()

        if movie_name:

            movies_list = hybrid_recommend(
                movie_name
            )[:10]

            print(
                "\n" + "=" * 60
            )

            print(
                "SEARCHED MOVIE:",
                movie_name
            )

            print(
                "Recommended Movies:",
                movies_list
            )

            print(
                "Total Movies:",
                len(movies_list)
            )

            print(
                "=" * 60
            )

            with ThreadPoolExecutor(max_workers=10) as executor:

                movie_ids = [
                    movie["movieId"]
                    for movie in movies_list
                ]

                results = executor.map(
                    get_movie_details,
                    movie_ids
                )

                for details in results:

                    if details:

                        recommendations.append(
                            details
                        )
                        
                if len(recommendations) == 0:

                    no_results = True        

            print(
                "TOTAL RECOMMENDATIONS:",
                len(recommendations)
            )

            print(
                "=" * 60 + "\n"
            )
            

    return render_template(
    "index.html",
    recommendations=recommendations,
    movie_name=movie_name,
    movie_titles=movie_titles,
    no_results=no_results
    
)

if __name__ == "__main__":
    app.run(debug=True)