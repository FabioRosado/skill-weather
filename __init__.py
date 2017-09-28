from opsdroid.matchers import match_regex

import requests
import logging


_LOGGER = logging.getLogger("opsdroid")


def get_weather(config):
    base_url = "http://api.openweathermap.org/data/2.5/"
    api_url = "weather?q={}&units={}&appid={}".format(
        config['city'], config['unit'], config['api-key'])
    weather_data = requests.get(base_url + api_url).json()
    return weather_data


@match_regex(r'(?:how|what)(?:\'s|s| is) the weather', case_sensitive=False)
async def weather(opsdroid, config, message):
    weather = get_weather(config)
    temp = weather['main']['temp']
    humidity = weather['main']['humidity']
    city = weather['name']
    status = weather['weather'][0]['main']

    await message.respond("It's currently {} degrees, {}% humidity "
                          "in {} and {} is forecasted for today".format(temp, humidity, city, status))


@match_regex(r'is it (?:cold|hot|warm|nice outside)', case_sensitive=False)
async def cold_outside(opsdroid, config, message):
    weather = get_weather(config)
    temp = weather['main']['temp']

    if temp < 10 or temp < 50 and config['unit'] == 'imperial':
        await message.respond("It's pretty cold today! It's currently "
                              "{} degrees outside".format(temp))
    elif temp > 10 < 19 or temp > 50 < 65:
        await message.respond("I think it's better if you take a "
                              "jacket with you today. It's currently "
                              "{} degrees outside".format(temp))
    elif temp > 19 < 23 or temp > 65 < 75:
        await message.respond("It's not too bad actually, it's currently "
                              "{} degrees outside".format(temp))
    elif temp > 23 or temp > 75:
        await message.respond("It's getting pretty hot, it's currently "
                              "{} degrees outside".format(temp))
