from django.shortcuts import render

# Create your views here.
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=f203e6337b6a87b4d2bc925a8c1b3e68').read()
        list_of_data = json.loads(source)

        data = {
            "city": city,
            "country_code" : str(list_of_data['sys']['country']),
            "coordinate" : str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp']) + ' °C',
            "pressure" : str(list_of_data['main']['pressure']) + ' Ba',
            "humidity" : str(list_of_data['main']['humidity']) + ' g/m³',
            'main' : str(list_of_data['weather'][0]['main']),
            'description' : str(list_of_data['weather'][0]['main']),
            'icon' : str(list_of_data['weather'][0]['icon']),
        }
        print(data)

    else:
        data = {}

    return render(request, "main/index.html", data)
