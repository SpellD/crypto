import requests
import datetime
from config import bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! Напиши мне название города!')


@dp.message_handler()
async def get_weather(message: types.Message):

    smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U00001F328",
        "Mist": "Туман \U00001F32B"
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()

        city = data['name']
        weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in smile:
            wd = smile[weather_description]
        else:
            wd = 'Посмотри в окно!'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length = sunset - sunrise

        await message.reply(f'***{datetime.datetime.now().strftime("%Y-%m-%d %H-%H-%S")}***\n'
                            f'Погода в городе: {city}\nТемпература: {weather}°C {wd}\n'
                            f'Влажность: {humidity}\nТемпература: {pressure} мм.рт.ст\nВетер: {wind} м/с\n'
                            f'Восход солнца: {sunrise}\nЗакат солнца: {sunset}\nПродолжительность дня: {length}\n'
                            f'***Хорошего дня!***'
                            )

    except Exception:
        await message.reply('\U00002620 Проверьте название города \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
