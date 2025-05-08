# Telegram Payment Bot for MLBB
import telebot
import requests
import hashlib
import time
from flask import Flask, request

# Bot configuration
BOT_TOKEN = '7663699162:AAFBc9Yy5ilib3ff0p3ncNecsmH9PgSLGOo'
API_URL = 'https://www.smile.one/smilecoin/api/'
UID = '1202586'
EMAIL = 'rcsexplaination@gmail.com'
UPI_ID = '7629088530@ptyes'
RAZORPAY_KEY = 'rzp_live_dl6YnaEbul9Rz1'
RAZORPAY_SECRET = 'MhJl2bsD11noOy5DTZVLkhJl'
ADMIN_ID = '8161279210'

bot = telebot.TeleBot(BOT_TOKEN)

# Generate sign
def generate_sign(params, key):
    sorted_params = sorted(params.items())
    sign_str = ''.join([f'{k}={v}&' for k, v in sorted_params]) + key
    return hashlib.md5(hashlib.md5(sign_str.encode()).hexdigest().encode()).hexdigest()

# Fetch products
def get_products():
    timestamp = int(time.time())
    params = {'uid': UID, 'email': EMAIL, 'product': 'mobilelegends', 'time': timestamp}
    sign = generate_sign(params, '992d767e3266edc7f46643b38fe8dc97')
    params['sign'] = sign
    response = requests.post(f'{API_URL}productlist', data=params)
    return response.json()

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Welcome! Enter your Game ID and Zone ID.')

# Verify username
@bot.message_handler(commands=['verify'])
def verify(message):
    bot.send_message(message.chat.id, 'Enter your username to verify:')

# Handle payments
def initiate_payment(amount):
    payment_link = f'https://razorpay.com/pay/{RAZORPAY_KEY}'
    return payment_link

# Order history
@bot.message_handler(commands=['history'])
def order_history(message):
    bot.send_message(message.chat.id, 'Fetching your order history...')

# Admin update price
@bot.message_handler(commands=['update_price'])
def update_price(message):
    if str(message.from_user.id) == ADMIN_ID:
        bot.send_message(message.chat.id, 'Send the new price pack details.')
    else:
        bot.send_message(message.chat.id, 'Access denied.')

# Run bot
bot.polling()

