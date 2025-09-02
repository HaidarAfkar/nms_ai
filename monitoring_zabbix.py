from typing import Final
from telegram.ext import CommandHandler, filters, MessageHandler, ContextTypes, Application, ContextTypes
from telegram import Update
import time
#from datetime import datetime
import re




TOKEN: Final = '7575343586:AAHvfhDFX2OuFCpkNa7m1bqFPwalLsewZqk'
BOT_USERNAME: Final = '@Morahelp_bot'



#Commands
async def start_command(update : Update, context : ContextTypes.DEFAULT_TYPE) :
    await update.message.reply('Hello! I am Transmission Bot!')
    
async def help_command(update : Update, context : ContextTypes.DEFAULT_TYPE) :
    await update.message.reply('Hello! I will Help You Soon!!')

async def custom_command(update : Update, context : ContextTypes.DEFAULT_TYPE) :
    await update.message.reply('Hello! Nice Custom Command')



#Handle Responses 
def handle_response(text: str, sender_username: str, groups: str) -> str:

    def Convertspace(string):
        li = list(string.split(" "))
        return li

    print(f'Thanks for your message, {sender_username}, dan group {groups}')
    print(type(groups))
    def Convertspace(string):
        li = list(string.split(" "))
        return li

    processed: str = text.lower()

    time.sleep(1)
    print(processed)
    if sender_username == None :
        return "Mohon maaf request kamu tidak bisa di lanjutkan, mohon isi username telegram kamu terlebih dahulu Terimakasih"
    else: 
        sender_username = sender_username

        return "Pastikan format yang kamu input sudah sesuai"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    sender_username: str = update.message.from_user.username

    print("Message : ", message_type)
    print("Text : ", text)
    print(f'User ({update.message.chat.id}, {sender_username}) in {message_type}: "{text}"')


    user_allowed = ['HaidarAfkar']

    groups = update.message.chat.id

    users = sender_username
    
    if message_type == 'private' and users in user_allowed:
        response: str = handle_response(text, sender_username, groups)
    else :
        pass
  # Pass sender_username here


    print('Bot:', response)
    await update.message.reply_text(response)



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot.. ')
    app = Application.builder().token(TOKEN).build()


    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))


    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    #Polls the bot
    print('Polling..')
    app.run_polling(poll_interval=3)







