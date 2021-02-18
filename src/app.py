import tkinter as tk
import os
import sys

#initialize the window
window = tk.Tk()

#create a label
title = tk.Label(window, text = "Website Blocker", font=("Helvetica", 18))
title.place(x=150,y=40)

#other stuff
window.title("Weblock")
window.geometry("500x350+480+150")
icon = tk.PhotoImage(file = 'src/icon.png')
window.iconphoto(False, icon)
window.mainloop()