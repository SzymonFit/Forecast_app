import requests
from tkinter import *

url='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
api_key='203d4cb81da56f71571200dbd79006c6'

canvas = Tk()
canvas.geometry("500x400")
canvas.title("Weather")

city = StringVar()

enter_city_label = Label(canvas, text="Enter city name", font='bold')
enter_city_label.pack()

search_city = Entry(canvas, textvariable=city)
search_city.pack()

search_button = Button(canvas, text= "Search", width=10, command=search)
search_button.pack()

city_label = Label(canvas, text="City: ", font="bold")
city_label.pack()

country_label = Label(canvas, text='Country: ', font="bold")
country_label.pack()

weather_conditions_label=Label(canvas, text="Weather conditions: ", font='bold')
weather_conditions_label.pack()

temperature_label = Label(canvas, text="Temperature:  (°C)", font="bold")
temperature_label.pack()

felt_temperature_label = Label(canvas, text="Felt temperature: (°C)", font='bold')
felt_temperature_label.pack()

pressure_label = Label(canvas, text="Pressure: (hPa)", font="bold")
pressure_label.pack()

humidity_label = Label(canvas, text='Humidity: (%)', font='bold')
humidity_label.pack()

wind_speed_label = Label(canvas, text='Wind speed: (m/s)', font='bold')
wind_speed_label.pack()

canvas.mainloop()

def get_weather(city):
    data_get_weather = requests.get(url.format(city,api_key))
    if data_get_weather:
        data_to_json = data_get_weather.json()
        city = data_to_json['name']
        country = data_to_json['sys']['country']
        conditions = data_to_json['weather'][0]['main']
        celsius_temperature = int(data_to_json['main']['temp'] - 273)
        celsius_felt_temperature = int(data_to_json['main']['feels_like'] - 273)
        pressure_level = data_to_json['main']['pressure']
        humidity_level = data_to_json['main']['humidity']
        wind_speed = data_to_json['wind']['speed']
        all_information = (("City: " + city), ("Country: " + country), ("Weather Conditions: " + conditions), ("Temperature: " + str(celsius_temperature)), ("Felt temperature: " + str(celsius_felt_temperature)), ("Pressure: " + str(pressure_level)), ("Humidity: " + str(humidity_level)), ("Wind speed: " + str(wind_speed)))
        return all_information
    else:
        return None

def search():
    city = search_city.get()
    weather = get_weather(city)
    if weather:
        city_label['text'] = '{}'.format(weather[0])
        country_label['text'] = '{}'.format( weather[1])
        weather_conditions_label['text'] = '{}'.format(weather[2])
        temperature_label['text'] = '{} °C'.format(weather[3])
        felt_temperature_label['text'] = '{} °C'.format(weather[4])
        pressure_label['text'] = '{} hPa'.format(weather[5])
        humidity_label['text'] = '{}%'.format(weather[6])
        wind_speed_label['text'] = '{}m/s'.format(weather[7])
    else:
        return "Error"