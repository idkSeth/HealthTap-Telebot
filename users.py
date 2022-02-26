#Manage users, retival of user data, registration, etc

from sqlite3 import *

def is_registered(chat_id):
    db = connect("database.db")
    c = db.cursor()
    c.execute('''SELECT user_id FROM users WHERE chat_id = chat_id''')
    user_id = c.fetchone()
    return user_id != None