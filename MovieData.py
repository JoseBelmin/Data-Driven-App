# TMDB API
import requests
import tmdbsimple as tmdb
import urllib.request
from urllib.error import HTTPError, URLError
from PIL import Image, ImageTk

# Key
API_KEY = "f38ca6a78610b61ecefac1679d06c740"

# Calling database
tmdb.API_KEY = API_KEY
tmdb.REQUESTS_TIMEOUT = 10
tmdb.REQUESTS_SESSION = requests.Session()

# Structuring movie information
class movie_data:
    def __init__(self, name, year, poster_path, overview, rating, id):
        self.name = name
        self.year = year
        self.poster_path = poster_path
        self.overview = overview
        self.rating = rating
        self.id = id
# Summoning poster from TMDB
def download_image(url, id):
    try:
        poster_name = f"posters/{id}.jpg"
        urllib.request.urlretrieve(url, poster_name)
    except (HTTPError, URLError):
        return "Assets\PnA.png"
    
    # Poster styleing
    basewidth = 320
    img = Image.open(poster_name).convert("RGB")
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(poster_name)
    return poster_name
# Summoning movie data from TMDB
def get_data(query):
    search = tmdb.Search()
    search.movie(query=f"{query}")
    obj_lst = []
    
    for result in search.results:
        try:
            result["release date"]
            
            obj_lst.appened(movie_data(result["name"], result["release date"], result["poster_path"],
                                       result["overview"], result["vote_average"], result["id"]))
        except KeyError:
            obj_lst.appened(movie_data(result["name"], result["release date"], result["poster_path"],
                                       result["overview"], result["vote_average"], result["id"],
                                       "Not Available"))
    return obj_lst