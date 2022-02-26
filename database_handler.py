#Manage users, retival of user data, registration, etc

from sqlite3 import *

def is_registered(chat_id):
    db = connect("database.db")
    c = db.cursor()
    c.execute('''SELECT user_id FROM users WHERE chat_id = chat_id''')
    user_id = c.fetchone()
    db.close()
    return user_id != None

def register_user(chat_id,info):
    db = connect("database.db")
    c = db.cursor()
    c.execute('''INSERT INTO users (chat_id) VALUES (:chat_id)''', {"chat_id":chat_id})
    user_id = get_user_id(chat_id)
    info.update({"user_id":user_id})
    c.execute('''INSERT INTO user_info (user_id, name, dob, ic) VALUES (:user_id, :name, :dob, :ic)''', info)
    db.commit()
    db.close()

def get_user_id(chat_id):
    db = connect("database.db")
    c = db.cursor()
    user_id = c.execute('''SELECT user_id FROM users WHERE chat_id = chat_id''').fetchone()
    db.close()
    return user_id

def get_user_name(user_id):
    db = connect("database.db")
    c = db.cursor()
    name = c.execute('''SELECT name FROM user_info WHERE user_id = user_id''').fetchone()
    db.close()
    return name[0]

def get_user_dob(user_id):
    db = connect("database.db")
    c = db.cursor()
    dob = c.execute('''SELECT dob FROM user_info WHERE user_id = user_id''').fetchone()
    db.close()
    return dob[0]

def get_user_ic(user_id):
    db = connect("database.db")
    c = db.cursor()
    ic = c.execute('''SELECT ic FROM user_info WHERE user_id = user_id''').fetchone()
    db.close()
    return ic[0]