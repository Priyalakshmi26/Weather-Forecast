from django.shortcuts import render,redirect
from django.http import HttpResponse
import urllib.request
import json
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=65b814a422d6b4a7feb3df3c81e1cd84').read()
        url2 = json.loads(url)
        data = {

                "country": city,
                "description": url2['weather'][0]['description'],
                "temperature": url2['main']['temp'],
                "pressure": url2['main']['pressure'],
                "humidity":url2['main']['humidity'],
                "icon": url2['weather'][0]['icon'],
                "feels":url2['main']['feels_like'],
            }
    else:
        city = None
        data = {
            "country": None,
            "description": None,
            "temperature": None,
            "pressure": None,
            "humidity":None,
            "icon": None,
            "feels":None,
        }
    print(data['icon'])
    return render(request, 'index.html', {"city": city, "data" :data})