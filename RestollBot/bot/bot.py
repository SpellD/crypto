import pandas as pd
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bs4 import BeautifulSoup as BS

from config import bot_token

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


# Стартовое меню
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global hello, pic

    # Удаление предыдущих сообщений
    try:
        await pic2.delete()
    except:
        pass
    try:
        await pic.delete()
    except:
        pass
    try:
        await hello.delete()
    except:
        pass
    try:
        await bot.delete_message(message.from_user.id, message_id=message.message_id)
    except:
        pass
    try:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    except:
        pass
    try:
        await msg.delete()
    except:
        pass
    try:
        await b.delete()
    except:
        pass
    try:
        await b1.delete()
    except:
        pass

    # Открываем картинку
    des = open('menu.jpg')
    
    # Приветствие
    name = message.from_user.first_name
    img = open('preview.jpg', 'rb')
    pic = await bot.send_photo(message.chat.id, img)
    hello = await bot.send_message(message.chat.id,
                           text=f'👋👋👋Добро пожаловать {name}👋👋👋! Этот телеграм бот был создан для того, чтобы '
                                f'помочь тебе выбрать товар📦 на сайте restoll.ru 🌐!')

    # Кнопки
    # keyboard = types.InlineKeyboardMarkup()
    # keyboard.add(types.InlineKeyboardButton(text="Ванны моечные", callback_data="1"))
    # keyboard.add(types.InlineKeyboardButton(text="Воздухоочистители", callback_data="2"))
    # keyboard.add(types.InlineKeyboardButton(text="Вытяжные зонты", callback_data="3"))
    # keyboard.add(types.InlineKeyboardButton(text="Модульные стелажные системы", callback_data="4"))
    # keyboard.add(types.InlineKeyboardButton(text="Подставки и подтоварники", callback_data="5"))
    # keyboard.add(types.InlineKeyboardButton(text="Полки", callback_data="6"))
    # keyboard.add(types.InlineKeyboardButton(text="Прилавки и модули", callback_data="7"))
    # keyboard.add(types.InlineKeyboardButton(text="Стелажи кухонные", callback_data="8"))
    # keyboard.add(types.InlineKeyboardButton(text="Столы для грязной и чистой посуды", callback_data="9"))
    # keyboard.add(types.InlineKeyboardButton(text="Столы и колоды разрубочные", callback_data="10"))
    # keyboard.add(types.InlineKeyboardButton(text="Столы кухонные", callback_data="11"))
    # keyboard.add(types.InlineKeyboardButton(text="Тележки производственные", callback_data="12"))
    # keyboard.add(types.InlineKeyboardButton(text="Тележки сервировочные", callback_data="13"))
    # keyboard.add(types.InlineKeyboardButton(text="Тележки-шпильки", callback_data="14"))
    # keyboard.add(types.InlineKeyboardButton(text="Шкафы для одежды", callback_data="15"))
    # keyboard.add(types.InlineKeyboardButton(text="Шкафы кухонные", callback_data="16"))
    # await message.answer("Меню", reply_markup=keyboard)
    mm = types.InlineKeyboardMarkup()
    mm.add(types.InlineKeyboardButton(text="Меню", callback_data="back"))
    await message.answer(text='Restoll', reply_markup=mm)


# Меню
@dp.callback_query_handler(text='back')
async def send_random_value(call: types.CallbackQuery):
    global b1, pic2

    # Удаление предыдущих сообщений
    try:
        await pic2.delete()
    except:
        pass
    try:
        await hello.delete()
    except:
        pass
    try:
        await pic.delete()
    except:
        pass
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    except:
        pass
    try:
        await msg.delete()
    except:
        pass
    try:
        await b.delete()
    except:
        pass
    try:
        await b1.delete()
    except:
        pass
    
    # Открываем картинку
    img2 = open('menu.jpg', 'rb')
    pic2 = await call.message.answer_photo(img2)

    # Кнопки
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Ванны моечные", callback_data="1"))
    keyboard.add(types.InlineKeyboardButton(text="Воздухоочистители", callback_data="2"))
    keyboard.add(types.InlineKeyboardButton(text="Вытяжные зонты", callback_data="3"))
    keyboard.add(types.InlineKeyboardButton(text="Модульные стелажные системы", callback_data="4"))
    keyboard.add(types.InlineKeyboardButton(text="Подставки и подтоварники", callback_data="5"))
    keyboard.add(types.InlineKeyboardButton(text="Полки", callback_data="6"))
    keyboard.add(types.InlineKeyboardButton(text="Прилавки и модули", callback_data="7"))
    keyboard.add(types.InlineKeyboardButton(text="Стелажи кухонные", callback_data="8"))
    keyboard.add(types.InlineKeyboardButton(text="Столы для грязной и чистой посуды", callback_data="9"))
    keyboard.add(types.InlineKeyboardButton(text="Столы и колоды разрубочные", callback_data="10"))
    keyboard.add(types.InlineKeyboardButton(text="Столы кухонные", callback_data="11"))
    keyboard.add(types.InlineKeyboardButton(text="Тележки производственные", callback_data="12"))
    keyboard.add(types.InlineKeyboardButton(text="Тележки сервировочные", callback_data="13"))
    keyboard.add(types.InlineKeyboardButton(text="Тележки-шпильки", callback_data="14"))
    keyboard.add(types.InlineKeyboardButton(text="Шкафы для одежды", callback_data="15"))
    keyboard.add(types.InlineKeyboardButton(text="Шкафы кухонные", callback_data="16"))
    b1 = await call.message.answer("Меню", reply_markup=keyboard)


@dp.callback_query_handler()
async def send_random_value(call: types.CallbackQuery):
    global b

    # Удаление предыдущих сообщений
    try:
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    except:
        pass
    try:
        await b1.delete()
    except:
        pass

    global msg
    data1 = int(call.data)

    # Парсинг данных
    r = requests.get(menu.get(data1))
    html = BS(r.content, 'html.parser')
    a = html.find('div', class_="ajax_load cur block")
    name = a.findAll('a', class_="dark_link js-notice-block__title option-font-bold font_sm")
    link = a.findAll("div",
                     class_="col-lg-3 col-md-4 col-sm-6 col-xs-6 col-xxs-12 item item-parent "
                            "catalog-block-view__item js-notice-block item_block")
    price = a.findAll('span', class_="price_value")

    # Название товара
    n = []
    for i in name:
        n.append(i.text)

    # Ссылка на товар
    l = []
    for i in link:
        s = ('https://restoll.ru/' + str(
            i.find('a', class_="dark_link js-notice-block__title option-font-bold font_sm").get('href')))
        l.append(s)

    # Цена товара
    p = []
    for i in price:
        v = i.text + ' рублей'
        p.append(v)

    # Выравнивание значений
    n.extend([0, ] * (len(p) - len(n)))
    p.extend([0, ] * (len(n) - len(p)))

    for i, item in enumerate(p):
        if item == 0:
            p[i] = 'Нет в наличии'

    # Создание таблицы и объединение данных
    df = pd.DataFrame()
    df['Товар'] = n
    df['Цена'] = p
    df['Ссылка'] = l
    df['Дата'] = df['Товар'] + ' - ' + df['Цена'] + '\n' + df['Ссылка']

    data = []

    for i in df['Дата']:
        data.append(i)

    # Вывод данных
    data = ('\n\n'.join(data))
    msg = await call.message.answer(data)

    back = types.InlineKeyboardMarkup()
    back.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))
    b = await call.message.answer(text='🔙', reply_markup=back)


if __name__ == '__main__':
    executor.start_polling(dp)
