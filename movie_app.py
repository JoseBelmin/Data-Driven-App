import tkinter as tk
from tkinter import ttk

# API Key
## f38ca6a78610b61ecefac1679d06c740

# Global variables
font = ("Inter", 16)

# Create the main window
window = tk.Tk()
window.title("Mango Movies")
window.geometry("1366x1024")
window.option_add("*font", font)

# Logo image
logoImg = tk.PhotoImage(file="Images\Logo.png")
logoFrame = tk.Label(window, image=logoImg)
logoFrame.pack()

# Search bar
def search():
    query = searchBar.get()
    # Search logic here
    print(f"{query}")
# Entry field
searchBar = tk.Entry(window, width=50)
searchBar.pack()
# Search Button
searchButton = tk.Button(window, text="Search", command=search)
searchButton.pack()

label = tk.Label(window, text="Hello, World!")
label.pack()




# Run program
window.mainloop()