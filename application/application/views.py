from flask import request

from application import app

@app.route('/')
def hello():
    return "Hello from T"

@app.route('/contact')
def contact():
    return "Contact me at: 555-5555"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Do login"
    else:
        return "Show login form"