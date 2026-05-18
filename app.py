import os
import requests
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

#load env vars
app = Flask(__name__, template_folder="templates")
WEATHER_KEY = os.getenv('WEATHER_KEY')

def fetchWeatherAPI(city):
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric")
    weather_data = weather_response.json()
    temperature = weather_data['main']['temp']
    return [city, temperature]

@app.route('/')
def index():
    weather = fetchWeatherAPI("London")
    return render_template("index.html", city=weather[0], temp=weather[1])

if __name__ == '__main__':
    app.run()