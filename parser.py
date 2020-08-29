import requests

city = 'Москва'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=24d494d10738101bb970de2d513ccd17'
response = requests.get(url, headers={'Accept': 'application/json'})

data = response.json()
print(data['wind']['speed'])