from opsdroid.matchers import match_regex

import requests


base_url = "http://api.openweathermap.org/data/2.5/"


@match_regex(r'weather', case_sensitive=False)
async def weather(opsdroid, config, message):
    api_url = "weather?q={}&units={}&appid={}".format(
               config['city'], config['unit'], config['api-key'])
    weather = requests.get(base_url+api_url).json()

    temp = weather['main']['temp']
    humidity = weather['main']['humidity']
    city = weather['name']
    status = weather['weather'][0]['main']

    await message.respond("It's currently {} degrees, {}% humidity "
                          "in {} and {} is forecasted for today".format(temp, humidity, city, status))

