import requests
from tkinter import *

def search():
    pass

canvas = Tk()
canvas.geometry("500x400")
canvas.title("Weather")

city = StringVar()
city_search = Entry(canvas, textvariable=city)
city_search.pack()

search_button = Button(canvas, text= "Search", width=10, command=search)
search_button.pack()



canvas.mainloop()

