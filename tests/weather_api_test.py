import requests as r
import json

latitude = '35.962639'
longitude = '-83.916718'
WEATHER_API_KEY = "5aa3fcdc0875017ce99d12e1a39adc92"

exclude = ['minutely', 'hourly']
req_url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=%s&appid=%s" % (latitude, longitude, exclude, WEATHER_API_KEY)
params = {'units': 'imperial'}
req = r.request(url= req_url, params=params, method = 'get')
json_data = json.loads(req.text)
#forecast = json_data['hourly']['weather'][0]['description']

while True:
    forecast = [json_data['daily'][0]['weather'][0]['description']]
    for i in range(1, 7):
        forecast.append(json_data['daily'][i]['weather'][0]['description'])

        print(forecast)
    break



