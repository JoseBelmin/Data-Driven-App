# Tkinter
import tkinter as tk
import customtkinter as ctk
from tkinter import font
from PIL import Image, ImageTk
# TMDB API
import requests
import tmdbsimple as tmdb
from MovieData import get_data, download_image
from threading import Thread
import os
import sys

# Manually toggle between light and dark mode (Select line 15 then use ctrl + / to toggle)
ctk.set_appearance_mode("light")

# Open app window
window = ctk.CTk()
window.geometry("1113x744")
window.resizable(False, False)
window.iconbitmap("Assets\Mango.ico")
window.title("Mango Movies")

# Key
API_KEY = "f38ca6a78610b61ecefac1679d06c740" 
# Calling database
tmdb.REQUEST_TIMEOUT = 10
tmdb.REQUESTS_SESSION = requests.Session()
# Structuring movie information
search = tmdb.Search()
object_list = []
current_index = 1
poster_img = None

# Fonts
Lexend_path = "Fonts\Lexend-VariableFont_wght.ttf"
Lexend = font.Font(family="Lexend", size=12)
Inter_path = "Fonts\Inter-VariableFont_slnt,wght.ttf"
Inter = font.Font(family="Inter", size=12)

# Colors
Light = "#EBEBEB"
Dark = "#242424"
Color1 = "#FF9F1C"
Color2 = "#FFBF69"
Color3 = "#2EC4B6"
Color4 = "#5FE9DA"

# Home Content
def home():
    # App logo
    logoImg = ctk.CTkImage(light_image=Image.open("Assets\Logo - Light.png"),
                           dark_image=Image.open("Assets\Logo - Dark.png"),
                           size=(200, 115))
    logo = ctk.CTkLabel(window, image=logoImg, text="")
    logo.place(x=0, y=0)
    # Search Movie
    SLabel = ctk.CTkLabel(window,
                          text="S",
                          font=("Lexend", 32),
                          text_color=Color1)
    SLabel.place(x=452, y=255)
    earchLabel = ctk.CTkLabel(window,
                              text="earch",
                              font=("Lexend", 32),
                              text_color=(Dark, Light))
    earchLabel.place(x=472, y=255)

    MLabel = ctk.CTkLabel(window,
                          text="M",
                          font=("Lexend", 32),
                          text_color=Color3)
    MLabel.place(x=572, y=255)
    ovieLabel = ctk.CTkLabel(window,
                             text="ovie",
                             font=("Lexend", 32),
                             text_color=(Dark, Light))
    ovieLabel.place(x=600, y=255)
    # Searchbar
    searchbutton = ctk.CTkButton(window,
                                 text="Search",
                                 font=("Lexend", 12),
                                 text_color=(Dark, Light),
                                 width=75,
                                 fg_color=(Color3, Color1),
                                 hover_color=(Color4, Color2),
                                 corner_radius=3)
    searchbutton.place(x=716, y=325)
    searchbar = ctk.CTkEntry(window,
                             font=("Inter", 12),
                             text_color=Dark,
                             width=400,
                             height=28,
                             fg_color="#FFFFFF",
                             border_color=Light,
                             corner_radius=3)
    searchbar.place(x=316, y=325)

def Info():
    # Information window
    search = ctk.CTkToplevel()
    
    search.geometry("1113x744")
    search.resizable(False, False)
    search.iconbitmap("Assets\Mango.ico")
    search.title("Movie Information")
    # Delete used cache
    def delete_used_cache():
        folder = "posters"
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)

    # Searching for a movie
    def search_title(event):
        def execute():
            global search, object_list, current_index
            delete_used_cache()
            loading_info.config(text="Checking database...")
            current_index
            query = searchbar.get()
            object_list = get_data(query)
            display_info()
        Thread(target=execute).start()
    # Next movie
    def next_movie():
        global current_index
        current_index += 1
        if current_index == len(object_list):
            current_index = 0
        display_info()
    # Previous movie
    def previous_movie():
        global current_index
        current_index -= 1
        if current_index < 0:
            current_index = len(object_list) - 1
        display_info()
    # Displaying information
    def display_info():
        def execute():
            global object_list, current_index, poster_img
            # When no movie is found
            if len (object_list) == 0:
                loading_info.config(text="No results found")
                return
            loading_info.config(text="Gathering movie information...")
            movie = object_list[current_index]
            img = download_image(f"https://api.themoviedb.org/3/movie/{movie_id}/images", movie.id)
            poster_img = ImageTk.PhotoImage(Image.open(img))
            poster_canvas.create_image(0, 0, image=poster_img, anchor="nw")
            desc_box.config(state="normal")
            desc_box.delete("1.0", "end")
            desc_box.insert("1.0", movie.overview)
            details_box.config(state=NORMAL)
            details_box.delete("1.0", "end")
            
            details_box.insert("1.0", f"Title: {movie.title}\n\n"
                                      f"Release Date: {movie.release_date}\n\n"
                                      f"Rating: {movie.vote_average}\n\n"
                                      f"ID: {movie.id}")
            loading_info.config(text="Result {current_index + 1} out of {len(object_list)}")
            description_box.config(state="disabled")
            details_box.config(state="disabled")
        Thread(target=execute).start()
        
        
        

home()
window.mainloop()