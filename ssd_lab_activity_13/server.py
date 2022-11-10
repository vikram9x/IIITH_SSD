import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_login import (LoginManager, login_manager, login_user, logout_user, login_required, UserMixin)


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secret'
app.debug = True

db = SQLAlchemy(app)
login_manager = LoginManager()

login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

@app.route("/user/signup", methods = ["POST"])
def signup():
    if request.method == "POST":
        req = request.get_json()
        db.session.add(User(name=req["name"], email=req["email"], password=req["password"]))
        db.session.commit()
    return ""

@app.route("/user/signin", methods = ["POST"])
def signin():
    if request.method == "POST":
        req = request.get_json()
        email = req["email"]
        password = req["password"]
        user = User.query.filter_by(email=email).first()
        if user != None:
            if user.password == password:
                login_user(user)
                return jsonify({"status":200, "reason":"Logged in"})
            else:
                return jsonify({"status":500, "reason":"Incorrect password"})
        else:
            return jsonify({"status":500, "reason":"Incorrect email"})
    return jsonify({"status":500, "reason":"GET method used"})

@app.route("/user/signout", methods = ["GET"])
def signout():
    logout_user()
    return jsonify({"status":200, "reason":"Logged out"})

if "__main__" == __name__:
    app.run(host="127.0.0.1", port="4000", debug=True)