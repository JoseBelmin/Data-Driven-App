import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps
from tkinter.font import Font

# API Key
## f38ca6a78610b61ecefac1679d06c740

# Create the main window
window = tk.Tk()
window.minsize(1133, 744)
window.title("Mango Movies")

# Background image
bgImg = Image.open("Assets\Background.png")
bg_tk = ImageTk.PhotoImage(bgImg)

bgLabel = ttk.Label(window,
                    image=bg_tk)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

# Font Families
Lexend = Font(family="Lexend", size=12)
Inter = Font(family="Inter", size=12)

# Logo image
logoImg = Image.open("Assets\logo.png").resize((150, 100))
logo_tk = ImageTk.PhotoImage(logoImg)

logoLabel = ttk.Label(window, 
                      image=logo_tk)
logoLabel.pack(side="left", anchor="nw", fill="x", expand=True, padx=(30, 0), pady=(0, 0))

# Search bar
def search():
    query = searchBar.get()
    # Search logic here
    print(f"{query}")
# Entry field
searchBar = ctk.CTkEntry(window, 
                         width=150,
                         height=35,
                         text_color="#000000",
                         fg_color="#FFFFFF",
                         border_color="#FFFFFF",
                         corner_radius=6)
searchBar.pack(side="left", anchor="ne", expand=False, pady=(35, 0))
# Search Button
searchButton = ctk.CTkButton(window, 
                             text="Search",
                             text_color="#FFFFFF",
                             font=(Lexend, 12, "bold"),
                             command=search,
                             width=70,
                             height=35,
                             fg_color="#FF9F1C",
                             hover_color="#FFBF69",
                             corner_radius=6)
searchButton.pack(side="right", anchor="ne", expand=False, padx=(0, 30), pady=(35, 0))

# parent
parent = ttk.Frame(window)
parent.rowconfigure(10, weight=1)
parent.columnconfigure(10, weight=1)
parent.pack(fill="both", expand=True)




# Run program
window.mainloop()