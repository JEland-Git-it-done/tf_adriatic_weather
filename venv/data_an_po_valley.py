import pandas as pd; import numpy as np
import datetime as datetime
import json; import requests
import matplotlib.pyplot as plt; import matplotlib.dates as mdates
#Initialise this file by importing pandas and matplot, datetime using pip install x
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
#t1 = prepare_data(ferrara, "ferrara")
#df_ferrara = t1
#t2 = prepare_data(ferrara, "ferrara")
#df_ferrara = df_ferrara.append(t2)
#print(df_ferrara)
#print(t1)


#Uses csv files provided in the work book, found here https://github.com/Apress/python-data-analytics-2e/blob/master/

df_asti=pd.read_csv("asti.csv")
df_bologna=pd.read_csv("bologna.csv")
df_cesena=pd.read_csv("cesena.csv")
df_faenza=pd.read_csv("faenza.csv")
df_ferrara=pd.read_csv("ferrara.csv")
df_mantova=pd.read_csv("mantova.csv")
df_milano=pd.read_csv("milano.csv")
df_piacenza=pd.read_csv("piacenza.csv")
df_ravenna=pd.read_csv("ravenna.csv")
df_torino=pd.read_csv("torino.csv")

dist = [df_ravenna['dist'][0],
     df_cesena['dist'][0],
     df_faenza['dist'][0],
     df_ferrara['dist'][0],
     df_bologna['dist'][0],
     df_mantova['dist'][0],
     df_piacenza['dist'][0],
     df_milano['dist'][0],
     df_asti['dist'][0],
     df_torino['dist'][0]
]
temp_max = [df_ravenna['temp'].max(),
     df_cesena['temp'].max(),
     df_faenza['temp'].max(),
     df_ferrara['temp'].max(),
     df_bologna['temp'].max(),
     df_mantova['temp'].max(),
     df_piacenza['temp'].max(),
     df_milano['temp'].max(),
     df_asti['temp'].max(),
     df_torino['temp'].max()
]
temp_min = [df_ravenna['temp'].min(),
     df_cesena['temp'].min(),
     df_faenza['temp'].min(),
     df_ferrara['temp'].min(),
     df_bologna['temp'].min(),
     df_mantova['temp'].min(),
     df_piacenza['temp'].min(),
     df_milano['temp'].min(),
     df_asti['temp'].min(),
     df_torino['temp'].min()
]
hum_min = [df_ravenna['humidity'].min(),
     df_cesena['humidity'].min(),
     df_faenza['humidity'].min(),
     df_ferrara['humidity'].min(),
     df_bologna['humidity'].min(),
     df_mantova['humidity'].min(),
     df_piacenza['humidity'].min(),
     df_milano['humidity'].min(),
     df_asti['humidity'].min(),
     df_torino['humidity'].min()
]
hum_max = [df_ravenna['humidity'].max(),
     df_cesena['humidity'].max(),
     df_faenza['humidity'].max(),
     df_ferrara['humidity'].max(),
     df_bologna['humidity'].max(),
     df_mantova['humidity'].max(),
     df_piacenza['humidity'].max(),
     df_milano['humidity'].max(),
     df_asti['humidity'].max(),
     df_torino['humidity'].max()
]

#print(df_name.shape) to see rows of data, considered unneccessary
def temp_trend_city(df_city):

    y1 = df_city["temp"]
    x1 = df_city["day"]
    fig, ax = plt.subplots()
    plt.xticks(rotation=70)
    title_obj = plt.title(df_city["city"][0])

    ax.plot(x1,y1,"r")
    plt.show()

def temp_tred_groupcities():
    y1 = df_ravenna['temp']
    x1 = df_ravenna['day']
    y2 = df_faenza['temp']
    x2 = df_faenza['day']
    y3 = df_cesena['temp']
    x3 = df_cesena['day']
    y4 = df_milano['temp']
    x4 = df_milano['day']
    y5 = df_asti['temp']
    x5 = df_asti['day']
    y6 = df_torino['temp']
    x6 = df_torino['day']
    fig, ax = plt.subplots()

    plt.plot(x1, y1, 'r', x2, y2, 'r', x3, y3, 'r')
    plt.plot(x4, y4, 'g', x5, y5, 'g', x6, y6, 'g')
    plt.show()

def max_temp_seadistance():
    plt.plot(dist, temp_max, "ro")
    plt.show()

def max_temp_distance_relational():
    x = np.array(dist)
    y = np.array(temp_max)
    x1=x[x<100]
    x1=x1.reshape((x1.size,1))
    y1=y[x<100]
    x2=x[x>50]
    x2=x2.reshape((x2.size,1))
    y2=y[x>50]
    from sklearn.svm import SVR
    svr_lin1 = SVR(kernel="linear", C=1e3)
    svr_lin2 = SVR(kernel="linear", C=1e3)
    svr_lin1.fit(x1, y1)
    svr_lin2.fit(x2, y2)
    xp1 = np.arange(10,100,10).reshape((9,1))
    xp2 = np.arange(50,400,50).reshape((7,1))
    yp1 = svr_lin1.predict(xp1)
    yp2 = svr_lin2.predict(xp2)
    plt.plot(xp1, yp1, c="r", label="Strong sea effect")
    plt.plot(xp2, yp2, c="b", label="Light sea effect")
    plt.axis((0, 400, 27, 32))
    plt.scatter(x, y, c="k", label="data")
    plt.show()


df_list = [df_milano, df_ferrara, df_asti, df_bologna, df_cesena,
           df_faenza, df_mantova, df_piacenza, df_ravenna, df_torino]
max_temp_distance_relational()
#for i in range(len(df_list)):
#    temp_trend_city(df_list[i])
print(df_cesena)

