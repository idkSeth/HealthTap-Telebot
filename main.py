from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext

TOKEN = "5279956152:AAF6chL3IBeNIcX6YFBAUXYX8l_0TfaiSsI"

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

def send_image(chat_id, image)
    updater.bot.send_photo(chat_id, photo=open(image, rb))

def send_text(chat_id, text):
    up

def stop()
    updater.stop()