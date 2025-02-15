import telebot
from telebot import types

bot = telebot.TeleBot('7517338129:AAEYSjyfYqFaZaotR6wQUSTxZHsfzrLbo_I')


@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Где поесть?')
    button2 = types.KeyboardButton('Проживание')
    button3 = types.KeyboardButton('Где погулять?')
    button4 = types.KeyboardButton('Где побывать?')
    button5 = types.KeyboardButton('Где выпить кофе?')
    keyboard.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, 'Навигатор по Альметьевску\nЧто вас интересует?', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Где поесть?':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/11121/almetyevsk/chain/vkusno_i_tochka/214710996368/?ll=52.293844%2C54.899257&sctx=ZAAAAAgBEAAaKAoSCR42kZkLJkpAERQJpppZc0tAEhIJuTZUjPM30D8RB3k9mBQfvz8iBgABAgMEBSgAOABA8VZIAWoCcnWdAc3MzD2gAQCoAQC9Ad7arCPCAQy4%2B%2F7MrgSmh9%2BUigaCAhdjaGFpbl9pZDooMjE0NzEwOTk2MzY4KYoCAJICAJoCDGRlc2t0b3AtbWFwcw%3D%3D&sll=52.293844%2C54.899257&sspn=0.046704%2C0.015669&z=15'))
        bot.send_message(message.chat.id, '<b>Вкусно - и точка</b>\n<b>Адрес:</b> ул. Ленина, 100, 3 этаж\n              ул. Ленина, 21А\n<b>Время работы:</b> 7.00 - 00.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/rostic_s/30440996063/?indoorLevel=3&ll=52.274091%2C54.899414&z=16'))
        bot.send_message(message.chat.id, '<b>Rostic\'s</b>\n<b>Адрес:</b> ул. Ленина, 100\n<b>Время работы:</b> 9.00 - 22.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/11121/almetyevsk/chain/dodo_picca/70891266502/?ll=52.301685%2C54.901693&sll=52.301685%2C54.901690&z=14'))
        bot.send_message(message.chat.id, '<b>Додо пицца</b>\n<b>Адрес:</b> ул. Ленина, 94\n              ул. Герцена, 3В\n<b>Время работы:</b> 8.00 - 00.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/chaykhana_1/1806638615/?ll=52.280733%2C54.899881&z=14'))
        bot.send_message(message.chat.id, '<b>Чайхана №1</b>\nРесторан узбекской кухни.\n<b>Адрес:</b> ул. Ленина, 94\n<b>Время работы:</b> пн-чт: 11.00 - 00.00\n                             пт: 11.00 - 1.00\n                             сб: 12.00 - 1.00\n                             вс: 12.00 - 00.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/lamore_mio/1700541520/?ll=52.265261%2C54.897466&z=17'))
        bot.send_message(message.chat.id, '<b>L\'amore Mio</b>\nПиццерия, предлагающая большой выбор пиццы и роллов\n<b>Адрес:</b> ул. Зифы Балакиной, 3\n<b>Время работы:</b> 10.00 - 23.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/sayuri/16262801449/?ll=52.264918%2C54.897750&z=14'))
        bot.send_message(message.chat.id, '<b>Саюри</b>\nКафе, где можно найти широкий выбор блюд, включая пиццу, роллы и десерты.\n<b>Адрес:</b> ул. Зифы Балакиной, 7\n<b>Время работы:</b> пн-чт, вс: 11.00 - 23.00\n                             пт-сб: 11.00 - 00.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/syrovarnya/65139470669/?ll=52.289424%2C54.897868&z=15'))
        bot.send_message(message.chat.id, '<b>Сыроварня</b>\n<b>Адрес:</b> ул. Ленина, 69А\n<b>Время работы:</b> 11.00 - 23.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/giviko/31436970162/?ll=52.304424%2C54.902556&z=14'))
        bot.send_message(message.chat.id, '<b>Гивико</b>\nРесторан грузинской кухни.\n<b>Адрес:</b> ул. Пушкина, 66\n<b>Время работы:</b> пн-чт, вс:11.00 - 23.00\n                             пт-сб: 11.00 - 00.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/inari/1534749748/?ll=52.297449%2C54.896905&z=17'))
        bot.send_message(message.chat.id, '<b>Инари</b>\nСуши-бар, пиццерия.\n<b>Адрес:</b> ул. Мусы Джалиля, 11А\n<b>Время работы:</b> пн-чт, вс - 9.00 - 23.00\n                             пт-сб: 9.00 - 23.45', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/neft/142818082482/?ll=52.253709%2C54.909050&z=15'))
        bot.send_message(message.chat.id, '<b>Нефть</b>\nРесторан, значительную часть меню составляют блюда с морепродуктами.\n<b>Адрес:</b> проспект Изаила Зарипова, 25/1\n<b>Время работы:</b> пн-чт, вс - 11.00 - 23.00\n                             пт-сб: 11.00 - 00.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/stary_ambar/1161143011/?ll=52.314385%2C54.905184&z=15'))
        bot.send_message(message.chat.id, '<b>Старый амбар</b>\n<b>Адрес:</b> проспект Габдуллы Тукая, 25\n<b>Время работы:</b> пн-чт, вс - 11.00 - 23.00\n                             пт-сб: 11.00 - 1.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/dzhigit/24685268399/?ll=52.272947%2C54.899596&z=15'))
        bot.send_message(message.chat.id, '<b>Джигит</b>\nРесторан грузинской кухни.\n<b>Адрес:</b> ул. Ленина, 100, этаж 2\n<b>Время работы:</b> 10.00 - 22.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/sakura/1744405302/?ll=52.309400%2C54.903766&z=15'))
        bot.send_message(message.chat.id, '<b>Сакура</b>\nРесторан японской кухни.\n<b>Адрес:</b> ул. Ленина, 15Б\n<b>Время работы:</b> 8.00 - 21.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/khinkalnaya/136913076629/?ll=52.276119%2C54.893271&z=14'))
        bot.send_message(message.chat.id, '<b>Хинкальная</b>\nКафе грузинской кухни.\n<b>Адрес:</b> ул. Шевченко, 21Б\n<b>Время работы:</b> 11.00 - 23.00', parse_mode='HTML', reply_markup=markup)

    elif message.text == 'Где выпить кофе?':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/murmur_kofe/87776196986/?ll=52.291257%2C54.898776&z=14'))
        bot.send_message(message.chat.id, '<b>Мурмур Кофе</b>\n<b>Адрес:</b> ул. Ленина, 55\n<b>Время работы:</b> будни: 7.45 - 22.00\n                             выходные: 9.00 - 22.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/eklernaya/84906953386/?ll=52.289424%2C54.897868&z=16'))
        bot.send_message(message.chat.id, '<b>Эклерная</b>\n<b>Адрес:</b> ул. Ленина, 69А\n<b>Время работы:</b> будни: 7.30 - 19.30\n                             выходные: 9.00 - 21.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/binkharts/128145335404/?ll=52.268044%2C54.900291&z=16'))
        bot.send_message(message.chat.id, '<b>Бинхартс</b>\n<b>Адрес:</b> ул. Ленина, 102\n<b>Время работы:</b> будни: 8.00 - 00.00\n                             выходные: 9.00 - 00.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/sayuri_time/23013813577/?ll=52.299283%2C54.901836&z=14'))
        bot.send_message(message.chat.id, '<b>Саюри Time</b>\n<b>Адрес:</b> ул. Ленина, 33\n<b>Время работы:</b> будни: 7.30 - 21.00\n                             выходные: 9.00 - 22.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/coffee_dream/55994072059/?ll=52.310116%2C54.904015&z=14'))
        bot.send_message(message.chat.id, '<b>Coffee Dream</b>\n<b>Адрес:</b> ул. Ленина, 11\n<b>Время работы:</b> будни: 8.00 - 22.00\n                             выходные: 9.00 - 22.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/kofeynya_19_61/158746933203/?ll=52.296332%2C54.901430&z=16'))
        bot.send_message(message.chat.id, '<b>Кофейня 19\'61</b>\n<b>Адрес:</b> ул. Ленина, 46\n<b>Время работы:</b> будни: 9.00 - 22.00\n                             выходные: 10.00 - 22.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/ppsladosti/86437001098/?ll=52.308376%2C54.904077&z=14'))
        bot.send_message(message.chat.id, '<b>Ппсладости</b>\n<b>Адрес:</b> ул. Ленина, 13\n<b>Время работы:</b> пн-сб: 9.00 - 21.00\n                             вс: 9.00 - 20.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/chb/142935605770/?ll=52.301121%2C54.903539&z=15'))
        bot.send_message(message.chat.id, '<b>Чб</b>\n<b>Адрес:</b> ул. Ленина, 30\n<b>Время работы:</b> будни: 7.30 - 21.30\n                             выходные: 8.30 - 21.30', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/mental_coffee_dine/231466331567/?ll=52.292945%2C54.904318&z=16'))
        bot.send_message(message.chat.id, '<b>Mental coffee dine</b>\n<b>Адрес:</b> ул. Гагарина, 23\n<b>Время работы:</b> 8.00 - 22.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/coffee_like/48843378010/?ll=52.274017%2C54.899379&z=16'))
        bot.send_message(message.chat.id, '<b>Coffee Like</b>\n<b>Адрес:</b> ул. Ленина, 100, этаж 1\n<b>Время работы:</b> 10.00 - 22.00', parse_mode='HTML', reply_markup=markup)

    elif message.text == 'Где погулять?':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/gorodskoy_park_imeni_60_letiya_nefti_tatarstana/1895901299/?ll=52.301753%2C54.898454&z=15'))
        bot.send_message(message.chat.id, '<b>Городской парк имени 60-летия нефти Татарстана</b>\nПарк культуры и отдыха, украшенный малыми архитектурными формами из природных материалов и имеющий более 30 аттракционов.\n<b>Адрес:</b> ул. Радищева, 22\n<b>Время работы:</b> 6.00 - 22.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/park_zdorovye/217654464411/?ll=52.266589%2C54.897839&z=17'))
        bot.send_message(message.chat.id, '<b>Парк Здоровье</b>\nВ парке есть множество возможностей для отдыха и развлечений: детские и спортивные площадки, фонтан, планетарий. Кроме того, здесь есть кафе и магазины. Расположен недалеко от ТРЦ Панорама.', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/kaskad_prudov/9646509808/?ll=52.288948%2C54.906381&z=15'))
        bot.send_message(message.chat.id, '<b>Каскад прудов</b>\nПарк, имеющий большую детскую площадку и скейт-парк. Также здесь есть пруд, в котором плавают утки и лебеди. Вечером парк красиво подсвечивается. Расположен рядом с мечетью имени Ризы Фахретдина.', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/komsomolskiy_park/140217063970/?ll=52.310354%2C54.912223&z=16'))
        bot.send_message(message.chat.id, '<b>Комсомольский парк</b>\nМесто для прогулок и занятий спортом, есть спортивные и детские площадки. В парке растёт множество деревьев. Расположен недалеко от Высшей школы нефти.', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/park_shamsinur/225817864546/?ll=52.278019%2C54.903446&z=16'))
        bot.send_message(message.chat.id, '<b>Парк Шамсинур</b>\nРасположен вдоль реки Бигашка. Здесь есть детские и спортивные площадки.', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/skver_yashlek/111406888889/?ll=52.250985%2C54.904515&z=17'))
        bot.send_message(message.chat.id, '<b>Сквер Яшьлек</b>\nЗдесь есть игровые и спортивные площадки, а также здесь часто проводятся различные мероприятия.', parse_mode='HTML', reply_markup=markup)

    elif message.text == 'Проживание':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/kubyz/35656182705/?ll=52.314612%2C54.914033&z=16'))
        bot.send_message(message.chat.id, '<b>ГОСТИНИЦА "Кубыз" 3 звезды</b>\nЗдесь созданы все условия для комфортного проживания: кондиционер, холодильник, телевизор, фен, утюг, посуда, отопление, доступ в интернет. Уборка каждый день. Также есть камера хранения. <em>Цена - от 4500 руб. за ночь.</em>\n<b>Адрес:</b> ул. Советская, 222Б', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/deluxe/1783362010/?ll=52.317429%2C54.903208&z=13'))
        bot.send_message(message.chat.id, '<b>ГОСТИНИЦА "DeLuxe" 3 звезды</b>\nЗдесь созданы все условия для комфортного проживания: кондиционер, холодильник, телевизор, фен, утюг, отопление, доступ в интернет. Уборка каждый день. Также есть ресторан и парковка. <em>Цена - от 3300 руб. за ночь.</em>\n<b>Адрес:</b> ул. Ризы Фахретдина, 32', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/delyuks/1196755926/?ll=52.324008%2C54.905328&z=16'))
        bot.send_message(message.chat.id, '<b>ГОСТИНИЦА "Делюкс" 3 звезды</b>\nЗдесь созданы все условия для комфортного проживания: кондиционер, холодильник, телевизор, фен, утюг, посуда, отопление, доступ в интернет. Уборка каждый день. Также есть ресторан и парковка. <em>Цена - от 5000 руб. за ночь.</em>\n<b>Адрес:</b> ул. 8 Марта, 23Б', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/viardo/5242204471/?ll=52.306360%2C54.901934&z=13'))
        bot.send_message(message.chat.id, '<b>ГОСТИНИЦА "Виардо" 3 звезды</b>\nЗдесь созданы все условия для комфортного проживания: кондиционер, телевизор, ресторан, тренажёрный зал, сауна, доступ в интернет. Также есть парковка. <em>Цена - от 3542 руб. за ночь.</em>\n<b>Адрес:</b> ул. Тимирязева, 17', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/sultanmurat/1140285839/?ll=52.286459%2C54.904976&z=16'))
        bot.send_message(message.chat.id, '<b>ГОСТИНИЦА "Султанмурат" 3 звезды</b>\nЗдесь созданы все условия для комфортного проживания: кондиционер, холодильник, телевизор, утюг, отопление, доступ в интернет. Также есть парковка и бассейн. <em>Цена - от 3500 руб. за ночь.</em>\n<b>Адрес:</b> ул. Нефтяников, 10', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/frisson/16761711364/?ll=52.306285%2C54.888962&z=16'))
        bot.send_message(message.chat.id, '<b>ГОСТИНИЦА "Frisson" 2 звезды</b>\nЗдесь созданы все условия для комфортного проживания: кондиционер, холодильник, телевизор, фен, утюг, посуда, отопление, доступ в интернет. Также есть парковка. <em>Цена - от 2800 руб. за ночь.</em>\n<b>Адрес:</b> Индустриальная ул., 23Ж', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/neftyanik/1000816058/?ll=52.302852%2C54.909835&z=13'))
        bot.send_message(message.chat.id, '<b>ГОСТИНИЦА "Нефтяник" 3 звезды</b>\nЗдесь созданы все условия для комфортного проживания: кондиционер, холодильник, телевизор, фен, утюг, отопление. Также есть камера хранения, ресторан и парковка. <em>Цена - от 5408 руб. за ночь.</em>\n<b>Адрес:</b> ул. Толстого, 11', parse_mode='HTML', reply_markup=markup)

    elif message.text == 'Где побывать?':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/almetyevskiy_tatarskiy_gosudarstvenny_dramaticheskiy_teatr/1081797399/?ll=52.298003%2C54.900529&z=16'))
        bot.send_message(message.chat.id, '<b>Альметьевский Татарский Государственный Драматический Театр</b>\n<b>Адрес:</b> ул. Ленина, 37\n<b>Время работы:</b> вт-сб: 10.30 - 18.30', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/panorama/1266499918/?ll=52.274017%2C54.899379&z=16'))
        bot.send_message(message.chat.id, '<b>ТРЦ Панорама</b>\nВ этом торговом центре вы найдёте множество развлечений, таких как кафе, кинотеатр, развлекательный центр и магазины.\n<b>Адрес:</b> ул. Ленина, 100\n<b>Время работы:</b> 10.00 - 22.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/plyazh/220770244824/?ll=52.340178%2C54.887523&z=11'))
        bot.send_message(message.chat.id, '<b>Альметьевский городской пляж</b>\nПляж имеет озеро, в котором можно купаться летом, песчаный берег, кафе и другие развлечения.\n<b>Время работы:</b> пн-чт, вс: 9.00 - 00.00\n                             пт-сб: 9.00 - 2.00', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/11121/almetyevsk/geo/ploshchad_neftyanikov/1520639038/?ll=52.280135%2C54.899110&z=18'))
        bot.send_message(message.chat.id, '<b>Площадь Нефтяников</b>\nГлавная площадь Альметьевска. Здесь часто проводятся различные мероприятия, а зимой стоит Центральня ёлка. Также рядом с площадью находится дворец культуры "Нефтьче".', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/almetyevskskiy_gosudarstvenny_neftyanoy_institut/74690493260/?ll=52.318583%2C54.913143&z=16'))
        bot.send_message(message.chat.id, '<b>Альметьевский государственный технологический университет Высшая школа нефти</b>\nБудучи образовательным учреждением, он также является местом притяжения жителей и туристов, так как занимает огромную территорию, обустроенную, как парк.\n<b>Адрес:</b> ул. Советская, 210', parse_mode='HTML', reply_markup=markup)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📍 На карте", url='https://yandex.ru/maps/org/gorodskoy_park_imeni_60_letiya_nefti_tatarstana/1895901299/?ll=52.301753%2C54.898454&z=15'))
        bot.send_message(message.chat.id, '<b>Городской парк имени 60-летия нефти Татарстана</b>\nПарк культуры и отдыха, имеющий более 30 аттракционов для детей и взрослых.\n<b>Адрес:</b> ул. Радищева, 22\n<b>Время работы:</b> 6.00 - 22.00', parse_mode='HTML', reply_markup=markup)

bot.polling()
