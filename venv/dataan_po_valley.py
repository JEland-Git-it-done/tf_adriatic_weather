import numpy as np; import pandas as pd
import datetime
import json; import requests
#Initialise this file by import pandas, using pip install x
#This program aims to analyse the links between weather data, relating to the adriatic ocean and the po valley
#Initialises JSON data to city name
ferrara = json.loads(requests
                     .get('http://api.openweathermap.org/data/2.5/'
                          '?q=Ferrara,IT&appid=5807ad2a45eb6bf4e81d137dafe74e15').text)
print(ferrara)



