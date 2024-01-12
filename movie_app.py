import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

# API Key
## f38ca6a78610b61ecefac1679d06c740

# Global variables
font = ("Inter", 16)

# Create the main window
window = tk.Tk()
window.title("Mango Movies")
window.geometry("1133x744")
window.option_add("*font", font)

# Logo image
logoImg = Image.open("Images\logo.png")
logo_tk = ImageTk.PhotoImage(logoImg)

logoLabel = ttk.Label(window, image=logo_tk)
logoLabel.pack()

# Search bar
def search():
    query = searchBar.get()
    # Search logic here
    print(f"{query}")
# Entry field
searchBar = ctk.CTkEntry(window, width=50)
searchBar.pack()
# Search Button
searchButton = ctk.CTkButton(window, text="Search", command=search)
searchButton.pack()

label = ctk.CTkLabel(window, text="Hello, World!")
label.pack()




# Run program
window.mainloop()