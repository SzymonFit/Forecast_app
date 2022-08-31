import requests
from tkinter import *
from configparser import ConfigParser


url='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
api_key='203d4cb81da56f71571200dbd79006c6'

def get_weather(city):
    outcome = requests.get (url.format(city,api_key))
    if outcome:
        json = outcome.json()
        city = json['name']
        country = json['sys']['country']
        conditions = json['weather'][0]['main']
        kelvin_temperature = json['main']['temp']
        celsius_temprerature = kelvin_temperature - 273
        
        



def search():
    city = city.text.get()
    weather = get.weather(city)

canvas = Tk()
canvas.geometry("500x400")
canvas.title("Weather")

city = StringVar()
city_search = Entry(canvas, textvariable=city)
city_search.pack()
search_button = Button(canvas, text= "Search", width=10, command=search)
search_button.pack()
location = Label(canvas, text='Location: ', font="bold")
location.pack()
weather_conditions=Label(canvas, text="Weather conditions: ", font='bold')
temperature = Label(canvas, text="Temperature: ", font="bold")
temperature.pack()
felt_temperature = Label(canvas, text="Felt temperature: ", font='bold')
felt_temperature.pack()
pressure = Label(canvas, text="Pressure: ", font="bold")
pressure.pack()
humidity = Label(canvas, text='Humidity: ', font='bold')
humidity.pack()
wind_speed = Label(canvas, text='Wind speed: ', font='bold')
wind_speed.pack()

canvas.mainloop()