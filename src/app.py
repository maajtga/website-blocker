import tkinter as tk
import os
import sys

#initialize the window
window = tk.Tk()

#other stuff
window.title("Weblock")
window.geometry("500x350+480+150")
icon = tk.PhotoImage(file = 'src/icon.png')
window.iconphoto(False, icon)

#create labels
title = tk.Label(window, text = "Website Blocker", font=("Helvetica", 18))
title.place(x=150,y=40)

info = tk.Label(window, text = "Make sure to run this program by right clicking \n and running as administrator. Enter website name below \n make sure to only put the webite name followed by the .com.\n For example \n youtube.com - Correct \n www.youtube.com - Wrong", font=("Sans Serif", 10))
info.place(x=65,y=100)

#change directory to "C:\Windows\System32\Drivers\etc"
os.chdir(r"C:\Windows\System32\Drivers\etc")

#main loop
window.mainloop()