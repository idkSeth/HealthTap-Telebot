#Telegram Bot

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from database_handler import *

TOKEN = "5142611206:AAHvFcOMWyzDBavdAq8vbVDXlUnublwmj-k"

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi! I am the HealthTap Bot! \n You can send '/start' to start a chat with me and select a category of help or just type your question. \n /user - Get's the user info \n /register - Login with your details to use the service \n /help - Help menu \n /human - Connects you to a live chat. \n /appointments - Appointments menu. View past appointments, manage future appointments and even make an appointment here \n /medicine - Medicine menu. You can view the medicines that are prescribed to you find more information about them or request refills. \n /bills View and manage bills")

def start(update: Update, context: CallbackContext) -> None:
    if update.message.chat.type == 'private':
        registered = is_registered(update.message.from_user.id)
    if registered:
        update.message.reply_text("Hi! I am the HealthTap Bot! Select an option from the menu below or type your question. \n /appointments - Appointments menu \n /medicine - Medicine menu \n /bills - Manage bills")
    else:
        update.message.reply_text("You are not registered yet, to use this service please register by using /register.")

def user(update: Update, context: CallbackContext) -> None:
    user_id = get_user_id(update.message.chat.id)
    update.message.reply_text(f"Name: {get_user_name(user_id)} DOB: {get_user_dob(user_id)} IC: {get_user_ic(user_id)}")
    
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def register(update: Update, context: CallbackContext):
    update.message.reply_text("Register user")
    global store, state
    store = {"name":None, "dob":None, "ic":None}
    state = "name"
    context.bot.send_message(chat_id=update.message.chat.id, text="Enter your full name")
    return CONFIRM

def confirm(update: Update, context: CallbackContext):
    update.message.reply_text("Ok")
    global info
    info = update.message.text
    context.bot.send_message(chat_id=update.message.chat.id, text=f"{info} Is that correct?")
    return CONFIRM2

def confirm2(update: Update, context: CallbackContext):
    global state, info,store
    update.message.reply_text("Ok")
    cmd = str(update.message.text)
    if cmd.lower() == "y" or cmd.lower() == "yes":
        store.update({state:info})
        if state == "name":
            context.bot.send_message(chat_id=update.message.chat.id, text="Enter your dob in the format dd/mm/yyyy")
            state = "dob"
            return CONFIRM
        elif state == "dob":
            context.bot.send_message(chat_id=update.message.chat.id, text="Enter your IC")
            state = "ic"
            return CONFIRM
        elif state == "ic":
            context.bot.send_message(chat_id=update.message.chat.id, text="Registration successful")
            register_user(update.message.from_user.id, store)
            return ConversationHandler.END
    else:
        if state == "name":
            context.bot.send_message(chat_id=update.message.chat.id, text="Enter your full name")
        elif state == "dob":
            context.bot.send_message(chat_id=update.message.chat.id, text="Enter your dob in the format dd/mm/yyyy")
        else:
            context.bot.send_message(chat_id=update.message.chat.id, text="Enter your IC")
        return CONFIRM

def done(update: Update, context: CallbackContext) -> int:
    context.bot.send_message(chat_id=update.message.chat.id, text="Registration unsuccessful")
    return ConversationHandler.END

REGISTER_NAME, REGISTER_DOB, REGISTER_IC, CONFIRM, CONFIRM2, DONE  = range(6)

def bills(update: Update, context: CallbackContext) -> None:
    u_id = get_user_id(update.message.chat.id)
    bills = get_user_bills(u_id)
    update.message.reply_text("Your bills")    
    for i in bills:
        context.bot.send_message(chat_id=update.message.chat.id, text=f"{i[0]} Amount: {i[1]} Date: {i[2]} Info: {i[3]}")

def medicine(update: Update, context: CallbackContext) -> None:
    u_id = get_user_id(update.message.chat.id)
    user_med = get_user_medicine(u_id)
    update.message.reply_text("Your prescribed medicines, select one for more information and options")
    for i in user_med:
        context.bot.send_message(chat_id=update.message.chat.id, text=f"Dosage: {i[1]} Frequency: {i[2]} Info: {i[3]}")
        
def appointments(update: Update, context: CallbackContext) -> None:
    u_id = get_user_id(update.message.chat.id)
    appointments = get_user_appointments(u_id)
    update.message.reply_text("Your appointments, select one for more options")
    for i in appointments:
        context.bot.send_message(chat_id=update.message.chat.id, text=f"{i[0]} Date: {i[1]} Location: {i[2]} Status: {i[3]} Info: {i[4]}")
    

def human(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("To continue with a live chat select a support category below")
          
def main() -> None:
    updater = Updater(TOKEN)


    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("user", user))
    dispatcher.add_handler(CommandHandler("bills", bills))
    dispatcher.add_handler(CommandHandler("medicine", medicine))
    dispatcher.add_handler(CommandHandler("appointments", appointments))
    dispatcher.add_handler(CommandHandler("human", human))
    
    conv_handler = ConversationHandler(
            entry_points = [CommandHandler("register", register)],
            states = {
                CONFIRM:[MessageHandler(Filters.text, confirm)],
                CONFIRM2:[MessageHandler(Filters.text, confirm2)],
                },
            fallbacks=[MessageHandler(Filters.regex('^Done$'), done)]
    )
            
    
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
    close()

if __name__ == '__main__':
    main()