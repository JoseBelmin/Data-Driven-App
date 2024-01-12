import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps
from tkinter import font

# API Key
## f38ca6a78610b61ecefac1679d06c740

# Create the main window
window = ctk.CTk()
window.geometry("1133x744")
window.title("Mango Movies")

# Font Families
Lexend = font.Font(family="Lexend", size=12)
Inter = font.Font(family="Inter", size=12)


# Logo image
logoImg = Image.open("Icons\logo.png")
logo_tk = ImageTk.PhotoImage(logoImg)

logoLabel = ttk.Label(window, 
                      image=logo_tk)
logoLabel.pack()

# Search bar
def search():
    query = searchBar.get()
    # Search logic here
    print(f"{query}")
# Entry field
searchBar = ttk.Entry(window, 
                      width=50)
searchBar.pack()
# Search Button
searchImg = Image.open("Icons\Search.png").resize((45, 45))
search_tk = ImageTk.PhotoImage(searchImg)

searchButton = ttk.Button(window, 
                          text="Search", 
                          command=search,
                          takefocus=False,
                          image=search_tk)
searchButton.pack()




# Run program
window.mainloop()