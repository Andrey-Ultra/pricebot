import telebot

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен бота
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот. Как дела?")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.polling()
