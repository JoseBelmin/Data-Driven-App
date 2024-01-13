import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps
from tkinter.font import Font

# API Key
## f38ca6a78610b61ecefac1679d06c740

# Create the main window
window = tk.Tk()
window.geometry("1133x744")
window.resizable(False, False)
window["background"] = "#CBF3F0"
window.title("logo Movies")

# Font Families
Lexend = Font(family="Lexend", size=12)
Inter = Font(family="Inter", size=12)

# Mango logo
logoImg = Image.open("Assets\logo.png").resize((216, 144))
logo_tk = ImageTk.PhotoImage(logoImg)

logoLabel = ttk.Label(window, 
                      image=logo_tk,
                      background="#CBF3F0")
logoLabel.pack()

# Search bar
def search():
    query = searchBar.get()
    ## Search logic here
    print(f"{query}")
# Entry field
searchBar = ctk.CTkEntry(window, 
                         width=150,
                         height=30,
                         text_color="#000000",
                         fg_color="#FFFFFF",
                         border_color="#FFFFFF",
                         corner_radius=6)
searchBar.pack()
# Search Button
searchButton = ctk.CTkButton(window, 
                             text="Search",
                             text_color="#FFFFFF",
                             font=(Lexend, 12, "bold"),
                             command=search,
                             width=70,
                             height=30,
                             fg_color="#FF9F1C",
                             hover_color="#FFBF69",
                             corner_radius=6)
searchButton.pack()



# Run program
window.mainloop()