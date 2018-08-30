import ephem
import datetime
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(bot, update):
    mytext = """Привет, {}!
Я просто бот и знаю только {}
    """.format(update.message.chat.first_name, '/start')
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)

def planets(bot, update):
    mytext = """Привет, {}!
Введи название планеты на английском {}
    """.format(update.message.chat.first_name, '/planet')
    logging.info('Пользователь {} нажал /planet'.format(update.message.chat.username))
    update.message.reply_text(mytext)
    planets_chat()

def planets_chat(bot, update):
    name_planet = update.message.text
    logging.info(name_planet)
    if name_planet == 'Mars':
        sky = ephem.Mars()
    elif name_planet == 'Mercury':
        sky = ephem.Mercury()
    elif name_planet == 'Venus':
        sky = ephem.Venus()
    elif name_planet == 'Earth':
        sky = ephem.Earth()
    elif name_planet == 'Jupiter':
        sky = ephem.Jupiter()
    elif name_planet == 'Saturn':
        sky = ephem.Saturn()
    elif name_planet == 'Uranus':
        sky = ephem.Uranus()
    elif name_planet == 'Neptune':
        sky = ephem.Neptune()
    elif name_planet == 'Pluto':
        sky = ephem.Pluto()
    else:
        update.message.reply_text('Wrong name planet')
    sky.compute(datetime.date.today())
    update.message.reply_text(ephem.constellation(sky))

def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    updtr = Updater(settings.TELEGRAM_API_KEY)
    updtr.dispatcher.add_handler(CommandHandler('start', start_bot))
    updtr.dispatcher.add_handler(CommandHandler('planet', planets))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, planets_chat))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    updtr.start_polling()
    updtr.idle()

if __name__ == "__main__":
    logging.info('Bot started')
    main()
