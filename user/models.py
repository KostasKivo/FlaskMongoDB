from flask import Flask,jsonify,request,session,redirect
from passlib.hash import pbkdf2_sha256
import uuid
from app import db

class User:

    def start_session(self,user):
            del user['password']
            session['logged_in'] = True
            session['user'] = user
            return jsonify(user), 200

    def signup(self):
        
        # Create the user
        user = {
            "_id":uuid.uuid4().hex,
            "username": request.form.get('name'),
            "password": request.form.get('password'),
            "email": request.form.get('email')
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        if db.users.find_one({ "email": user['email'] }):
            return jsonify({"error":"Email adress is already in use"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)


        return jsonify({"error": "Signup failed"}),400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):

        user = db.users.find_one( { "email": request.form.get('email') })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password'] ):
            return self.start_session(user)

        return jsonify('Invalid login credentials'), 401
