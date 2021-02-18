import tkinter as tk
import os
import sys

#initialize the window
window = tk.Tk()

#other stuff
window.title("Weblock")
window.geometry("500x350+480+150")

#change directory to "C:\Windows\System32\Drivers\etc"
os.chdir(r"C:\Windows\System32\Drivers\etc")

#create function to edit the hosts file
def EditHost():
    print("WOrking")

#create labels
title = tk.Label(window, text = "Website Blocker", font=("Helvetica", 18))
title.place(x=150, y=40)

directions = tk.Label(window, text = "Make sure to run this program by right clicking \n and running as administrator. Enter website name below \n make sure to only put the webite name followed by the .com.\n For example: \n youtube.com - Correct \n www.youtube.com - Wrong", font=("Sans Serif", 10))
directions.place(x=65, y=100)

info = tk.Label(window, text = "Enter Website Here", font=("Sans Serif", 12))
info.place(x=170, y=220)

#website variable 
website = tk.StringVar()

#create input box
web_entry = tk.Entry(window, textvariable = website, font = ('calibre', 10 ,'normal'))
web_entry.place(x=170, y=250)

#create submit button
sub_btn = tk.Button(window, text = 'Submit', command = EditHost)
sub_btn.place(x=215, y=280)

#main loop
window.mainloop()