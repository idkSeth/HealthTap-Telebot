#Telegram Bot

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from users import *

TOKEN = "5142611206:AAHvFcOMWyzDBavdAq8vbVDXlUnublwmj-k"

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi! I am the HealthTap Bot! \n You can send '/start' to start a chat with me and select a category of help or just type your question. \n /user - Get's the user info \n /register - Login with your details to use the service \n /help - Help menu \n /human - Connects you to a live chat. \n /appointments - Appointments menu. View past appointments, manage future appointments and even make an appointment here \n /medicine - Medicine menu. You can view the medicines that are prescribed to you find more information about them or request refills. \n /bills View and manage bills")

def start(update: Update, context: CallbackContext) -> None:
    if update.message.chat.type == 'private':
        registered = is_registered(update.message.from_user.id)
    if registered:
        update.message.reply_text("Hi! I am the HealthTap Bot! Select an option from the menu below or type your question. \n /appointments - Appointments menu \n /medicine - Medicine menu \n  /bills - Manage bills")
    else:
        update.message.reply_text("You are not registered yet, to use this service please register by using /register.")
    
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def register(update: Update, context: CallbackContext) -> None:
    pass
    

def main() -> None:
    updater = Updater(TOKEN)


    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("register", register))
    
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()