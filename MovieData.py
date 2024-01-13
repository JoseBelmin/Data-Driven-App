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

