import requests
from bs4 import BeautifulSoup as BS
from config import bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Получение токена
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

# Типы товаров
menu = {
    1: 'https://restoll.ru/catalog/vanny-moechnye-i-rukomoyniki/',
    2: 'https://restoll.ru/catalog/vozdukhoochistiteli/',
    3: 'https://restoll.ru/catalog/vytyazhnye-zonty/',
    4: 'https://restoll.ru/catalog/modulnye-stellazhnye-sistemy/',
    5: 'https://restoll.ru/catalog/podstavki-i-podtovarniki/',
    6: 'https://restoll.ru/catalog/polki/',
    7: 'https://restoll.ru/catalog/prilavki-i-moduli/',
    8: 'https://restoll.ru/catalog/stellazhi_kukhonnye/',
    9: 'https://restoll.ru/catalog/stoly-dlya-gryaznoy-i-chistoy-posudy/',
    10: 'https://restoll.ru/catalog/stoly-i-kolody-razrubochnye/',
    11: 'https://restoll.ru/catalog/stoly-kukhonnye/',
    12: 'https://restoll.ru/catalog/telezhki-proizvodstvennye/',
    13: 'https://restoll.ru/catalog/telezhki-servirovochnye/',
    14: 'https://restoll.ru/catalog/telezhki-shpilki/',
    15: 'https://restoll.ru/catalog/shkafy_dlya_odezhdy/',
    16: 'https://restoll.ru/catalog/shkafy-kukhonnye/'
}


# Меню
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, '---Выберите тип товаров---\n' +
                        '1.Ванны моечные\n' +
                        '2.Воздухоочистители\n' +
                        '3.Вытяжные зонты\n' +
                        '4.Модульные стелажные системы\n' +
                        '5.Подставки и подтоварники\n' +
                        '6.Полки\n' +
                        '7.Прилавки и модули\n' +
                        '8.Стелажи кухонные\n' +
                        '9.Столы для грязной и чистой посуды\n' +
                        '10.Столы и колоды разрубочные\n' +
                        '11.Столы кухонные\n' +
                        '12.Тележки производственные\n' +
                        '13.Тележки сервировочные\n' +
                        '14.Тележки-шпильки\n' +
                        '15.Шкафы для одежды\n' +
                        '16.Шкафы кухонные'
                        )

# Ввод пользователя
@dp.message_handler()
async def get_data(message: types.Message):

    global n, r

    # Проверка на ошибку числа
    try:
        n = int(message.text)
    except:
        await bot.send_message(message.from_user.id, 'Введите число')

    # Проверка на наличие в списке
    try:
        r = requests.get(menu.get(n))
    except:
        await bot.send_message(message.from_user.id, 'Такого типа товаров не существует')

    # Парсинг данных
    html = BS(r.content, 'html.parser')
    a = html.find('div', class_="ajax_load cur block")
    a = a.findAll("div",
                  class_="col-lg-3 col-md-4 col-sm-6 col-xs-6 col-xxs-12 item item-parent catalog-block-view__item "
                         "js-notice-block item_block")

    # Вывод товаров
    arr = []

    for i in a:
        t = i.text.strip().rsplit('\n')
        t = [value for value in t if value]
        price = str(t[2])
        price = price.replace(' ', '', 1)
        product = (t[0] + ' - ' + price)
        arr.append(product)

    data = ('\n\n'.join(arr))
    await bot.send_message(message.from_user.id, data)


if __name__ == '__main__':
    executor.start_polling(dp)
