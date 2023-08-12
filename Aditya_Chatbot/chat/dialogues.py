from datetime import *
import random
import requests
import chat.values as c
now = datetime.now()


class chat_conversation:
    def greeting():
        hour = int(now.hour)
        if hour>=0 and hour<12:
            print("Good Morning!")

        elif hour>=12 and hour<18:
            print("Good Afternoon!")
        else:
            print("Good evening!")

        print(random.choice(c.greeting))

    def day():
        days = now.strftime("%A, %B %d")
        print(f"Today is {days}")

    def get_weather():
        url = "https://api.openweathermap.org/data/2.5/weather?lat=27.699791&lon=85.274742&appid=03396dcc0f54b3576057b315d280879e"
        response_weather = requests.get(url)
        data_weather = response_weather.json()
        weather = data_weather["weather"][0]["main"]
        return weather
    
    def get_temperature():
        url = "https://api.openweathermap.org/data/2.5/weather?lat=27.699791&lon=85.274742&appid=03396dcc0f54b3576057b315d280879e"
        response = requests.get(url)
        data_temp = response.json()
        temperature = data_temp["main"]["temp"]
        temperature_in_Celsius = temperature - 273.15
        return temperature_in_Celsius
    
   
    def get_joke():
        url = "https://world-of-jokes1.p.rapidapi.com/v1/jokes"

        querystring = {"limit":"100","page":"1","sortBy":"score:desc"}

        headers = {
	    "X-RapidAPI-Key": "59577d9709msh7ac605c19cead92p1046b2jsnb891e449491c",
	    "X-RapidAPI-Host": "world-of-jokes1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())
    
    def get_news():
        url = "https://bing-news-search1.p.rapidapi.com/news"

        querystring = {"safeSearch":"Off","textFormat":"Raw"}

        headers = {
	        "X-BingApis-SDK": "true",
	        "X-RapidAPI-Key": "59577d9709msh7ac605c19cead92p1046b2jsnb891e449491c",
	        "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())
        
    def Exit():
        print(random.choice(c.close))
        exit()