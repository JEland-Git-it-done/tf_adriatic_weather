import numpy as np; import pandas as pd
import datetime as datetime
import json; import requests
#Initialise this file by importing pandas, datetime using pip install x
#This program aims to analyse the links between weather data, relating to the adriatic ocean and the po valley
#Initialises JSON data to city name
ferrara = json.loads(requests.get('http://api.openweathermap.org/data/2.5/weather?q=Ferrara,IT&APPID=f0fa4704d8ba2c556ca8238a82f9aa75').text)
#print(ferrara)
print("Testing JSON id keys ... \n", list(ferrara.keys()))
#Cleaner, vertical list


print("coords = ", ferrara["coord"])
print("weather =", ferrara["weather"])
print("base = ", ferrara["base"])
print("main = ", ferrara["main"])
print("visibility = ", ferrara["visibility"])
print("wind = ", ferrara["wind"])
print("clouds = ", ferrara["clouds"])
print("dt = ", ferrara["dt"])
print("sys = ", ferrara["sys"])
print("id = ", ferrara["id"])
print("name = ", ferrara["name"])
print("cod = ", ferrara["cod"])

coords =  {'lon': 11.62, 'lat': 44.84}
weather = [{'id': 741, 'main': 'Fog', 'description': 'fog', 'icon': '50d'}]
base =  "stations"
main =  {'temp': 276.86, 'feels_like': 274.75, 'temp_min': 274.15, 'temp_max': 279.26, 'pressure': 1027, 'humidity': 100}
visibility =  200
wind, clouds =  {'speed': 1.05, 'deg': 281}, {'all': 90}
dt =  1578407324
sys =  {'type': 1, 'id': 6761, 'country': 'IT', 'sunrise': 1578379847, 'sunset': 1578412070}
id =  3177090
name, cod =  "Ferrara", 200

def prepare_data(city, city_name):
    temp = [ ]
    humidity = [ ]
    pressure = [ ]
    description = [ ]
    dt = [ ]
    wind_speed = [ ]
    wind_deg = [ ]
    temp.append(city["main"]["temp"]-273.15)
    humidity.append(city["main"]["humidity"])
    pressure.append(city["main"]["pressure"])
    description.append(city["weather"][0]["description"])
    dt.append(city["dt"])
    wind_speed.append(city["wind"]["speed"])
    wind_deg.append(city["wind"]["deg"])
    headings = ["temp", "humidity", "pressure", "description", "dt", "wind_speed"
                , "wind_deg"]
    data = [temp, humidity, pressure, description, dt, wind_speed, wind_deg]
    df = pd.DataFrame(data, index=headings)
    city = df.T
    city["city"] = city_name
    city["day"] = city["dt"].apply(datetime.datetime.fromtimestamp)
    return city
t1 = prepare_data(ferrara, "ferrara")
print(t1)




