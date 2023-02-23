from telegram.ext import CommandHandler,MessageHandler,Filters,CallbackQueryHandler,Dispatcher
from telegram import Update,Bot
import os
from bot import count,send_image,start
from flask import Flask, request


Token=os.environ['TOKEN']


bot = Bot(Token)

app = Flask(__name__)


@app.route('/webhook', methods=["POST", "GET"])
def hello():
    if request.method == 'GET':
        return 'hi from Python2022I'
    elif request.method == "POST":
        data = request.get_json(force = True)
        
        dispacher: Dispatcher = Dispatcher(bot, update_queue=None, workers=0)
        update:Update = Update.de_json(data, bot)
    
        #update 
                
        dispacher.add_handler(CallbackQueryHandler(count))
        dispacher.add_handler(MessageHandler(Filters.photo,send_image))
        dispacher.add_handler(CommandHandler('start',start))


        
        dispacher.process_update(update)
        return 'ok'
