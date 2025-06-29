import requests
from django.shortcuts import render
import os
from dotenv import load_dotenv

def index(request):
    load_dotenv()
    weather = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = os.getenv("WEATHER_API_KEY")  # Replace with your API key
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        else:
            weather = {
                'city': city,
                'temperature': 'N/A',
                'description': 'City not found.',
                'icon': ''
            }

    return render(request, 'main/index.html', {'weather': weather})

