from flask import Flask, request
import telegram

app = Flask(__name__)
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telegram.Bot(token=TOKEN)

@app.route('/' + TOKEN, methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.sendMessage(chat_id=chat_id, text="Thanks for your message!")
    return 'ok'

@app.route('/')
def index():
    return 'Bot is running'

if __name__ == '__main__':
    app.run(threaded=True)
