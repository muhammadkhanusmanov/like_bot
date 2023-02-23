from telegram.ext import CallbackContext
from telegram import Update,InlineKeyboardMarkup,InlineKeyboardButton

import requests



def start(update: Update, context: CallbackContext):
    bot=context.bot 
    user_id=update.message.from_user.id
    text='Botga rasm yuboring uni kanalga baholash uchun jo\'natadi.'
    bot.sendMessage(user_id,text)

def send_image(update: Update, context: CallbackContext):
    bot=context.bot 
    message_id=update.message.message_id
    photo_id=update.message.photo[0].file_id
    payload={'image_id':message_id}
    response=requests.post('http://liketgbot.pythonanywhere.com/api/add_img/',json=payload)
    data=requests.get(f'http://liketgbot.pythonanywhere.com/api/{message_id}')
    data=data.json()
    likes=data['like']
    dislikes=data['dislike']
    text='Rasmni baholang'
    button=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=f'👍{likes}',callback_data=f'like {message_id}')],
            [InlineKeyboardButton(text=f'👎{dislikes}',callback_data=f'dislike {message_id}')]
        ]
    )
    bot.sendPhoto('@like_photo_img',photo_id,caption=text,reply_markup=button)



def count(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id=query.from_user.id
    message_id=query.message.message_id
    data,img = query.data.split(' ')
    img=int(img)
    bot = context.bot
    if data=='like':
        pyload={
            'user_id':user_id,
            'image_id':img
        }
        response=requests.post('http://liketgbot.pythonanywhere.com/api/add-like',json=pyload)
        data=requests.get(f'http://liketgbot.pythonanywhere.com/api/{img}').json()
        likes=data['like']
        dislikes=data['dislike']
        button=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=f'👍{likes}',callback_data=f'like {img}')
            ],
            [
                InlineKeyboardButton(text=f'👎{dislikes}',callback_data=f'dislike {img}')
                ]
            ]
            )
        bot.edit_message_reply_markup('@like_photo_img',message_id=message_id,reply_markup=button)

    else:
        pyload={
            'user_id':user_id,
            'image_id':img
        }
        response=requests.post('http://liketgbot.pythonanywhere.com/api/add-dislike',json=pyload)
        data=requests.get(f'http://liketgbot.pythonanywhere.com/api/{img}').json()
        likes=data['like']
        dislikes=data['dislike']
        button=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=f'👍{likes}',callback_data=f'like {img}')
            ],
            [
                InlineKeyboardButton(text=f'👎{dislikes}',callback_data=f'dislike {img}')
            ]
        ]
        )
        bot.edit_message_reply_markup('@like_photo_img',message_id=message_id,reply_markup=button)
        