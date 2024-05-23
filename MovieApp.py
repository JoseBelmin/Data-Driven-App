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
# ctk.set_appearance_mode("light")

# Open app window
window = ctk.CTk()
window.geometry("1113x744")
window.resizable(False, False)
window.iconbitmap("Assets\Mango.ico")
window.title("Mango Movies")

# Key
API_KEY = "f38ca6a78610b61ecefac1679d06c740" 
# Calling database
tmdb.REQUEST_TIMEOUT = 5
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
BungeeSpice_path = "Fonts\BungeeSpice-Regular.ttf"
BungeeSpice = font.Font(family="BungeeSpice", size=12)

# Colors
Light = "#EBEBEB"
Dark = "#242424"
Color1 = "#FF9F1C"
Color2 = "#FFBF69"
Color3 = "#2EC4B6"
Color4 = "#5FE9DA"



# Home Screen
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
    searchbar = ctk.CTkEntry(window,
                             font=("Inter", 12),
                             text_color=Dark,
                             width=400,
                             height=28,
                             fg_color="#FFFFFF",
                             border_color=Light,
                             corner_radius=3)
    searchbar.place(x=316, y=325)
    searchbutton = ctk.CTkButton(window,
                                 command=movie_info,
                                 text="Search",
                                 font=("Lexend", 12),
                                 text_color=(Dark, Light),
                                 width=75,
                                 fg_color=(Color3, Color1),
                                 hover_color=(Color4, Color2),
                                 corner_radius=3)
    searchbutton.place(x=716, y=325)

def movie_info():
    # Movie Information Screen
    search = ctk.CTkToplevel()
    search.geometry("1113x744")
    search.resizable(False, False)
    search.iconbitmap("Assets\Mango.ico")
    search.title("Movie Information")
    # App logo
    logoImg = ctk.CTkImage(light_image=Image.open("Assets\Logo - Light.png"),
                           dark_image=Image.open("Assets\Logo - Dark.png"),
                           size=(200, 115))
    logo = ctk.CTkLabel(search, image=logoImg, text="")
    logo.place(x=0, y=0)
    # Main content
    ## Background container
    infoBG = ctk.CTkLabel(search,
                          text="",
                          width=1000,
                          height=510,
                          fg_color=(Color4, Color2),
                          corner_radius=3)
    infoBG.place(x=57, y=150)
    # Movie Information
    movieName = ctk.CTkLabel(search,
                             text="Movie Name:",
                             font=("Lexend", 32),
                             text_color=Dark,
                             bg_color=(Color4, Color2))
    movieName.place(x=77, y=166)
    movieTitle = ctk.CTkLabel(search,
                              text=get_data(searchbar)[current_index].title,
                              font=("Lexend", 32),
                              text_color=Dark,
                              bg_color=(Color4, Color2))
    movieTitle.place(x=77, y=198)
    # Space for code to display movie name
    releaseDate = ctk.CTkLabel(search,
                               text="Year",
                               font=("Inter", 12),
                               text_color=Dark,
                               bg_color=(Color4, Color2))
    releaseDate.place(x=77, y=241)
    # Space for code to display movie release date
    ratings = ctk.CTkLabel(search,
                           text="Ratings",
                           font=("Inter", 12),
                           text_color=Dark,
                           bg_color=(Color4, Color2))
    ratings.place(x=153, y=241)
    # Space for code to display movie rating score
    movieID = ctk.CTkLabel(search,
                           text="Movie ID",
                           font=("Inter", 12),
                           text_color=Dark,
                           bg_color=(Color4, Color2))
    movieID.place(x=246, y=241)
    # Space for code to display movie id
    overView = ctk.CTkLabel(search,
                            text="Overview",
                            font=("Lexend", 18, "bold"),
                            text_color=Dark,
                            bg_color=(Color4, Color2))
    overView.place(x=77, y=345)
    ovBG = ctk.CTkLabel(search,
                        text="",
                        width=600,
                        height=275,
                        fg_color="#FFFFFF",
                        corner_radius=3)
    ovBG.place(x=77, y=373)
    # Space for code to display movie description
    poster_img = ctk.CTkImage(light_image=Image.open("Assets\PnA.png"),
                              dark_image=Image.open("Assets\PnA.png"),
                              size=(320, 450))
    poster = ctk.CTkLabel(search, image=display_movie_image, text="")
    poster.place(x=717, y=198)
            
home()
window.mainloop()