import telebot
from pytube import YouTube

# Replace with your actual Telegram Bot API Token
API_TOKEN = 6755178585:AAEYwdIelywvJFqWj5f5lk__luudi1r45KM
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me a YouTube video link to download it.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        bot.reply_to(message, "Video has been successfully downloaded!")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

bot.polling()
