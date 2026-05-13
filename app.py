import os
import requests
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder="templates")
WEATHER_KEY = os.getenv('')

@app.route('/')
def index():
    return render_template("index.html")