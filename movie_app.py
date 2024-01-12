import customtkinter as ctk
from tkinter import ttk

# API Key
## f38ca6a78610b61ecefac1679d06c740

# Global variables
font = ("Inter", 16)

# Create the main window
window = ctk.Ctk()
window.title("Mango Movies")
window.geometry("1366x1024")
window.option_add("*font", font)

# Logo image
logoImg = ctk.PhotoImage(file="Images\Logo.png")
logoFrame = ctk.Label(window, image=logoImg)
logoFrame.pack()

# Search bar
def search():
    query = searchBar.get()
    # Search logic here
    print(f"{query}")
# Entry field
searchBar = ctk.Entry(window, width=50)
searchBar.pack()
# Search Button
searchButton = ctk.Button(window, text="Search", command=search)
searchButton.pack()

label = ctk.Label(window, text="Hello, World!")
label.pack()




# Run program
window.mainloop()