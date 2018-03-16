import json

from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from api.config import Config
from domain.user.use_case.login import Login

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)


@app.route("/")
def welcome():
    return "api working."


@app.route("/user/auth", methods=['POST'])
def login():
    req = request.data.decode('utf-8')
    data = json.loads(req)
    try:
        user = Login().login(data['email'], data['password'])
        if user is None:
            return ('Not allowed', 401)
        else:
            return ('Logged', 200)
    except Exception as ex:
        return (str(ex), 400)

    @app.route("/user/register")
    def register(data):
        pass

    @app.route("/user/recover_password")
    def recover_password():
        pass
