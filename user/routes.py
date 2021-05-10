from flask import Flask
from app import app
from user.models import User    

#Include all user functions

@app.route('/user/register', methods =['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login', methods =['POST'])
def user_login():
    return User().login()