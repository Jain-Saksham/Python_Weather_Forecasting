import requests
import os
from datetime import datetime

user_api=os.environ['current_weather_data']
location=input("Enter the city name:")

complete_api_location="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link=requests.get(complete_api_location)
api_data=api_link.json()

if api_data['cod']=='404':
    print ("Invalid City:{}, Please check your city name.".format(location.upper()))
else:
    temp_city=((api_data['main']['temp'])-273.15)
    weather_desc=api_data['weather'][0]['description']
    hmdt=api_data['main']['humidity']
    wind_spd=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %y | %I:%M:%S %p")

print("----------------------------------------------------------")
print("Weather States for - {} || {}".format(location.upper(),date_time))
print("----------------------------------------------------------")        

print("Current Temperature : {:.2f} deg C".format(temp_city))
print("Current Weather Description : ",weather_desc)
print("Current Humidity Level :",hmdt,'%')
print("Current Wind Speed : ",wind_spd,'kmph')
