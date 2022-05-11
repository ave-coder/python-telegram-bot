import requests
from datetime import datetime
import telebot
from data import token


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%H:%M - %m.%d.%Y года')}\nСтоимость валюты: {sell_price}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет, друг! Напиши 'price',чтобы узнать цену BTC!")

    @bot.message_handler(content_types=["text"])
    def send_message(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%H:%M - %m.%d.%Y года')}\nСтоимость валюты: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Something was wrong..."
                )
        else:
            bot.send_message(
                message.chat.id,
                "Check the command!")

    bot.polling()


if __name__ == "__main__":
    telegram_bot(token)
