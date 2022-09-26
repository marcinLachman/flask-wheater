from flask import Blueprint, render_template

#import do json i url
import json
import urllib.request

#import do ustalenia timezone po lokalizacji
# import pip install timezonefinder
from timezonefinder import TimezoneFinder
#wyświetla aktualny czas po podaniu timezone lokalizacji
#trzeba zainstalować pip install pytz
import pytz
from datetime import datetime

from src.models import CityName

main = Blueprint('main', __name__)

API_URL = '33b8c88e24fd7520b39e5ab673cbc04c'

@main.route('/')
def index():

    fisrt_city_db = CityName.query.filter_by(id=1).first_or_404()
    fisrt_city = fisrt_city_db.city_name

    #link zawierający adres jason
    source_first = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={fisrt_city}&mode=json&units=metric&appid={API_URL}').read()
    #zamieniamy json w dictionry
    data_list_first = json.loads(source_first)

    #dane wyciągnięte z json i przypisane do zmiennych
    data_fisrt = {
        'temp': int(data_list_first['main']['temp']),
        'feels_like': int(data_list_first['main']['feels_like']),
        'pressure': str(data_list_first['main']['pressure']),
        'humidity': str(data_list_first['main']['humidity']),
        'icon': str(data_list_first['weather'][0]['icon']),
        'name': str(data_list_first['name']),
        'lon': float(data_list_first['coord']['lon']),
        'lat': float(data_list_first['coord']['lat']),
    }

    # tworzymy obiekt do lokalizcji
    obj = TimezoneFinder()
    #lokalizuję miejsce po podaniu współżędnych
    coutry_city= obj.timezone_at(lng=data_fisrt['lon'], lat=data_fisrt['lat'])

    #zamieniamy timezone na aktualną godzinę
    timezone = pytz.timezone(coutry_city)
    local_time = datetime.now(timezone)
    actual_time_first = local_time.strftime("%H:%M")

#------------------------------------------------------------------------------------------------

    second_city_db = CityName.query.filter_by(id=2).first_or_404()
    second_city = second_city_db.city_name

    #link zawierający adres jason
    source_second = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={second_city}&mode=json&units=metric&appid={API_URL}').read()
    #zamieniamy json w dictionry
    data_list_second = json.loads(source_second)

    #dane wyciągnięte z json i przypisane do zmiennych
    data_second = {
        'temp': int(data_list_second['main']['temp']),
        'feels_like': int(data_list_second['main']['feels_like']),
        'pressure': str(data_list_second['main']['pressure']),
        'humidity': str(data_list_second['main']['humidity']),
        'icon': str(data_list_second['weather'][0]['icon']),
        'name': str(data_list_second['name']),
        'lon': float(data_list_second['coord']['lon']),
        'lat': float(data_list_second['coord']['lat']),
    }

    # tworzymy obiekt do lokalizcji
    obj = TimezoneFinder()
    #lokalizuję miejsce po podaniu współżędnych
    coutry_city= obj.timezone_at(lng=data_second['lon'], lat=data_second['lat'])

    #zamieniamy timezone na aktualną godzinę
    timezone = pytz.timezone(coutry_city)
    local_time = datetime.now(timezone)
    actual_time_second = local_time.strftime("%H:%M")

#-----------------------------------------------------------------------------------

    third_city_db = CityName.query.filter_by(id=3).first_or_404()
    third_city = third_city_db.city_name

    #link zawierający adres jason
    source_third = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={third_city}&mode=json&units=metric&appid={API_URL}').read()
    #zamieniamy json w dictionry
    data_list_third = json.loads(source_third)

    #dane wyciągnięte z json i przypisane do zmiennych
    data_third= {
        'temp': int(data_list_third['main']['temp']),
        'feels_like': int(data_list_third['main']['feels_like']),
        'pressure': str(data_list_third['main']['pressure']),
        'humidity': str(data_list_third['main']['humidity']),
        'icon': str(data_list_third['weather'][0]['icon']),
        'name': str(data_list_third['name']),
        'lon': float(data_list_third['coord']['lon']),
        'lat': float(data_list_third['coord']['lat']),
    }

    # tworzymy obiekt do lokalizcji
    obj = TimezoneFinder()
    #lokalizuję miejsce po podaniu współżędnych
    coutry_city= obj.timezone_at(lng=data_third['lon'], lat=data_third['lat'])

    #zamieniamy timezone na aktualną godzinę
    timezone = pytz.timezone(coutry_city)
    local_time = datetime.now(timezone)
    actual_time_third = local_time.strftime("%H:%M")

    return render_template('index.html', 
        title='Aplikacja pogodowa',
        data_fisrt=data_fisrt, 
        data_second=data_second,
        data_third=data_third,
        actual_time_first=actual_time_first,
        actual_time_second=actual_time_second,
        actual_time_third=actual_time_third,
        fisrt_city=fisrt_city,
        second_city=second_city,
        third_city=third_city
    )