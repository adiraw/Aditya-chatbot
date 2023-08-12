import math
import requests
from chat.dialogues import chat_conversation as chat

def connection(data):

    if "day" in data:
        chat.day()

    elif "weather" in data:
        print(f"The current weather is {chat.get_weather()}.")
    
    elif "temperature" in data:
        print(f"The current temperature is {math.ceil(chat.get_temperature())} degree celcius.")
    
    elif "jokes" in data:
        print(f"Today's joke is{chat.get_joke()}.")
    
    elif "news" in data:
        print(f"Today's joke is{chat.get_news()}.")

    elif "exit" in data:
        chat.Exit()