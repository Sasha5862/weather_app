from flask import Flask, render_template, request
from googletrans import Translator
import requests

app = Flask(__name__)


# ee83021646e9aa38c6196bcf780b21c4

def feel( city=None, wind=None, icon=None, temp1=None, desc1=None, deg=None, feels_like1=None):
    pass


@app.route('/', methods=['post', 'get'])
def login(city=None, wind=None, icon=None, temp1=None, desc1=None, deg=None, feels_like1=None):

    try:
        if request.method == 'POST':
            city = request.form.get('text')  # запрос к данным формы

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=24d494d10738101bb970de2d513ccd17'
        response = requests.get(url, headers={'Accept': 'application/json'})

        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        wind = data['wind']['speed']
        deg = data['wind']['deg']
        icon = data['weather'][0]['icon']
        desc = data['weather'][0]['description']
        temp1 = int(temp)
        temp1 -= 273
        feels_like1 = int(feels_like)
        feels_like1 -= 273
        translator = Translator()
        desc1 = translator.translate(desc, src='en', dest='ru')

    except:
        print("Такого города нет")
    return render_template('index.html', city=city, wind=wind, icon=icon, temp1=temp1, desc1=desc1, deg=deg, feels_like1=feels_like1)




if __name__ == "__main__":
    app.run()
