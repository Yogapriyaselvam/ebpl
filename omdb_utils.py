# omdb_utils.py
import requests

def get_movie_details(title, api_key):

    url = f"http://www.omdbapi.com/?t={title.lower()}&plot=full&apikey={api_key}"
    res = requests.get(url).json()
    if res.get("Response") == "True":
        result = res.get("Plot", "N/A"), res.get("Poster", "N/A")
        plot = result[0]
        poster = result[1]
        print(poster)
        return plot, poster

    return "N/A", "N/A"


get_movie_details("avengers", "f63d86b6")