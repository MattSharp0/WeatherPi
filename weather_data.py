import json
import requests
import config


def get_weather():

    url = "https://api.weather.com/v2/pws/observations/current?stationId=" + \
        config.STATION+"&format=json&units=e&apiKey="+config.APIKEY
    response = requests.get(url)

    current_conditions = json.loads(response.text)
    # print(current_conditions)

    url = "https://api.weather.com/v3/wx/forecast/daily/5day?postalKey=" + \
        config.ZIPCODE+":US&units=e&language=en-US&format=json&apiKey="+config.APIKEY
    response = requests.get(url)

    forecast = json.loads(response.text)
    # print(forecast)

    conditions = {'temp': current_conditions['observations'][0]['imperial']['temp'],
                  'humidity': current_conditions['observations'][0]['humidity'],
                  'uv': current_conditions['observations'][0]['uv'],
                  'windSpeed': current_conditions['observations'][0]['imperial']['windSpeed'],
                  'windGust': current_conditions['observations'][0]['imperial']['windGust'],
                  'windDir': current_conditions['observations'][0]['winddir'],
                  'pressure': current_conditions['observations'][0]['imperial']['pressure'],
                  'precipRate': current_conditions['observations'][0]['imperial']['precipRate'],
                  'precipTotal': current_conditions['observations'][0]['imperial']['precipTotal'],
                  'date': (current_conditions['observations'][0]['obsTimeLocal'].split(' ')[0].split('-', 1)[1]),
                  'day': forecast['dayOfWeek'][0]}

    return(conditions)