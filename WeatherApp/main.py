import requests
import json
import pyttsx3
engine = pyttsx3.init()

city = input("Enter the name of the city:\n")

url = f"https://api.weatherapi.com/v1/current.json?key=ec6a9ebf460642b880430820240610&q={city}"
r = requests.get(url)

wdic = json.loads(r.text)

temp_c = wdic["current"]["temp_c"]
condition = wdic["current"]["condition"]["text"]
wind_kph = wdic["current"]["wind_kph"]
humidity = wdic["current"]["humidity"]
pressure_mb = wdic["current"]["pressure_mb"]
feelslike_c = wdic["current"]["feelslike_c"]
visibility_km = wdic["current"]["vis_km"]

print(f"City: {wdic['location']['name']}")
print(f"Temperature: {temp_c} °C")
print(f"Condition: {condition}")
print(f"Wind Speed: {wind_kph} km/h")
print(f"Humidity: {humidity}%")
print(f"Pressure: {pressure_mb} mb")
print(f"Feels Like: {feelslike_c} °C")
print(f"Visibility: {visibility_km} km")

message = (
    f"The current weather in {city} is as follows: "
    f"The temperature is {temp_c} degrees Celsius with {condition}. "
    f"The wind speed is {wind_kph} kilometers per hour. "
    f"The humidity is {humidity} percent. "
    f"Atmospheric pressure is {pressure_mb} millibars. "
    f"It feels like {feelslike_c} degrees Celsius. "
    f"Visibility is {visibility_km} kilometers."
)

engine.say(message)
engine.runAndWait()
