# Tkinter
import tkinter as tk
import customtkinter as ctk
from tkinter import font
from PIL import Image, ImageTk
# TMDB API
import requests
import tmdbsimple as tmdb
# from MovieData import MovieData, download_image
# from threading import Thread
# import os
# import sys

# ctk.set_appearance_mode("light")

# Open app window
window = ctk.CTk()
window.geometry("1113x744")
window.resizable(False, False)
window.iconbitmap("Assets\Mango.ico")
window.title("Mango Movies")

# Importing API
API_KEY = "f38ca6a78610b61ecefac1679d06c740" 

tmdb.REQUEST_TIMEOUT = 10
tmdb.REQUESTS_SESSION = requests.Session()

search = tmdb.Search()
object_list = []
current_index = 1
poster_img = None



# Fonts
Lexend_path = "Fonts\Lexend-VariableFont_wght.ttf"
Lexend = font.Font(family="Lexend", size=12)
Inter_path = "Fonts\Inter-VariableFont_slnt,wght.ttf"
Inter = font.Font(family="Inter", size=12)
# Home Content
## App logo
def home():
    logoImg = ctk.CTkImage(light_image=Image.open("Assets\Logo - Light.png"),
                        dark_image=Image.open("Assets\Logo - Dark.png"),
                        size=(200, 115))
    logo = ctk.CTkLabel(window, image=logoImg, text="")
    logo.place(x=0, y=0)
    ## Search Movie
    SLabel = ctk.CTkLabel(window,
                        text="S",
                        font=("Lexend", 32),
                        text_color="#FF9F1C")
    SLabel.place(x=452, y=225)
    earchLabel = ctk.CTkLabel(window,
                            text="earch",
                            font=("Lexend", 32),
                            text_color=("#242424", "#EBEBEB"))
    earchLabel.place(x=472, y=225)

    MLabel = ctk.CTkLabel(window,
                        text="M",
                        font=("Lexend", 32),
                        text_color="#2EC4B6")
    MLabel.place(x=572, y=225)
    ovieLabel = ctk.CTkLabel(window,
                            text="ovie",
                            font=("Lexend", 32),
                            text_color=("#242424", "#EBEBEB"))
    ovieLabel.place(x=600, y=225)
    ## Searchbar
    searchbutton = ctk.CTkButton(window,
                                text="Search",
                                font=("Lexend", 12),
                                text_color=("#242424", "#EBEBEB"),
                                width=75,
                                fg_color=("#2EC4B6", "#FF9F1C"),
                                hover_color=("#5FE9DA", "#FFBF69"),
                                corner_radius=3)
    searchbutton.place(x=716, y=300)
    searchbar = ctk.CTkEntry(window,
                            font=("Inter", 12),
                            width=400,
                            height=28,
                            fg_color="#FFFFFF",
                            border_color="#FFFFFF",
                            corner_radius=3)
    searchbar.place(x=316, y=300)
    # Navigation bar
    navbar = ctk.CTkFrame(window,
                        width=1113,
                        height=50,
                        fg_color=("#EBEBEB", "#242424"),
                        border_color=("#EBEBEB", "#242424"),
                        corner_radius=0,)
    navbar.pack(side="bottom", anchor="s", fill="x", expand=True)

    ## NavChildren
    homeImg = Image.open("Assets\Home.png").resize((26, 23))
    home_tk = ImageTk.PhotoImage(homeImg),

    navchild1 = ctk.CTkButton(navbar,
                            font=("Inter", 16),
                            text="Home",
                            text_color=("#242424", "#EBEBEB"),
                            width=90,
                            height=35,
                            fg_color=("#2EC4B6", "#FF9F1C"),
                            hover_color=("#5FE9DA", "#FFBF69"),
                            corner_radius=4,
                            image=home_tk)
    navchild1.place(x=385, y=0)

    trendImg = Image.open("Assets\Fire.png").resize((24, 23))
    trend_tk = ImageTk.PhotoImage(trendImg),

    navchild2 = ctk.CTkButton(navbar,
                            font=("Inter", 16),
                            text="Trending",
                            text_color=("#242424", "#EBEBEB"),
                            width=90,
                            height=35,
                            fg_color=("#2EC4B6", "#FF9F1C"),
                            hover_color=("#5FE9DA", "#FFBF69"),
                            corner_radius=4,
                            image=trend_tk)
    navchild2.place(x=500, y=0)

    savedImg = Image.open("Assets\Heart.png").resize((25, 23))
    saved_tk = ImageTk.PhotoImage(savedImg),

    navchild3 = ctk.CTkButton(navbar,
                            font=("Inter", 16),
                            text="Saved",
                            text_color=("#242424", "#EBEBEB"),
                            width=90,
                            height=35,
                            fg_color=("#2EC4B6", "#FF9F1C"),
                            hover_color=("#5FE9DA", "#FFBF69"),
                            corner_radius=4,
                            image=saved_tk)
    navchild3.place(x=630, y=0)

window.mainloop()
