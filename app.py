from flask import Flask,render_template,url_for,redirect,session
from functools import wraps
import pymongo

app = Flask(__name__)
app.debug = True
app.secret_key = "b55b6c62a2a76b92df857abdebb3a295"

#Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system


#Decorator
def login_required(f):
    @wraps(f) 
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            return redirect('/')
    return wrap 


def registered_while_logged(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if not 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            return redirect('/account/')
    return wrap



#User Routes
from user import routes  

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register/')
@registered_while_logged
def register():
        return render_template("register.html")

@app.route('/account/')
@login_required
def account():
    return render_template("account.html")

@app.route('/login/')
def login():
    return render_template("login.html")

