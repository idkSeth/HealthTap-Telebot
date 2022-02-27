#Manage users, retival of user data, registration, etc

from sqlite3 import *

def is_registered(tele_user_id):
    db = connect("database.db")
    c = db.cursor()
    c.execute('''SELECT user_id FROM users WHERE tele_user_id = tele_user_id''')
    user_id = c.fetchone()
    db.close()
    return user_id != None

def register_user(tele_user_id,info):
    db = connect("database.db")
    c = db.cursor()
    c.execute('''INSERT INTO users (tele_user_id) VALUES (:tele_user_id)''', {"tele_user_id":tele_user_id})
    user_id = get_user_id(tele_user_id)
    info.update({"user_id":tele_user_id})
    c.execute('''INSERT INTO user_info (user_id, name, dob, ic) VALUES (:user_id, :name, :dob, :ic)''', info)
    db.commit()
    db.close()

def get_user_id(tele_user_id):
    db = connect("database.db")
    c = db.cursor()
    user_id = c.execute('''SELECT user_id FROM users WHERE tele_user_id = tele_user_id''').fetchone()
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

def get_medicine_info(medicine_id):
    db = connect("database.db")
    c = db.cursor()
    medicine = c.execute('''SELECT name, type, description FROM medicine WHERE medicine_id = medicine_id''').fetchone()
    db.close()
    return medcine

def get_user_medicine(user_id):
    db = connect("database.db")
    c = db.cursor()
    medicines = c.execute('''SELECT medicine_id, dosage, frequency, info FROM user_medicine WHERE user_id = user_id''').fetchall()
    db.close()
    return medicines

def get_user_bills(user_id):
    db = connect("database.db")
    c = db.cursor()
    bills = c.execute('''SELECT bill_id, amount, date, info FROM user_bills WHERE user_id = user_id''').fetchall()
    db.close()
    return bills

def get_user_appointments(user_id):
    db = connect("database.db")
    c = db.cursor()
    appointments = c.execute('''SELECT appointment_id, date, location, status, info FROM user_appointments WHERE user_id = user_id''').fetchall()
    db.close()
    return appointments

def close():
    db.close()