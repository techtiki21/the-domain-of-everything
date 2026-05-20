import os
import requests
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

#load env vars
app = Flask(__name__, template_folder="templates")
WEATHER_KEY = os.getenv('WEATHER_KEY')
FINANCE_KEY = os.getenv('FINANCE_KEY')

def fetchAPI(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(response.status_code)

    data = response.json()
    return data

def weatherData(city):
    data = fetchAPI(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric")
    temp = data['main']['temp']
    lowHigh = f"{data['main']['temp_min']}/{data['main']['temp_max']}"
    feels = data['main']['feels_like']
    sky = data['weather'][0]['main']
    return {'city': city, 'temp': temp, 'feels': feels, 'sky': sky, 'lowHigh': lowHigh}

def financeData():
    data = fetchAPI(f"https://finnhub.io/api/v1/quote?symbol=SPY&token={FINANCE_KEY}")
    print(data)
    current = data['c']
    change = data['d']
    percent = round(data['dp'], 2)
    high = data['h']
    low = data['l']
    open = data['o']
    return {'current': current, 'day_change': change, "percentGrowth": percent,
            'stockHigh': high, 'stockLow': low, 'stockOpen': open}

@app.route('/')
def index():
    weather = weatherData("London")
    finance = financeData()
    return render_template("index.html", **weather, **finance)

if __name__ == '__main__':
    app.run()