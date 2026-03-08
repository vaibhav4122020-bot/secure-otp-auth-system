import hashlib
import random
from database import connect_db

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(email,password):
    db = connect_db()
    cur = db.cursor()
    hashed = hash_password(password)
    sql = "INSERT INTO users(email,password) VALUES (%s,%s)"
    cur.execute(sql,(email,hashed))
    db.commit()

def login_user(email,password):
    db = connect_db()
    cur = db.cursor()
    hashed = hash_password(password)
    sql = "SELECT * FROM users WHERE email=%s AND password=%s"
    cur.execute(sql,(email,hashed))
    user = cur.fetchone()
    return user

def generate_otp():
    return str(random.randint(100000,999999))
