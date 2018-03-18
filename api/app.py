import json
from flask import Flask, request
from domain.user.use_case.login import Login
from domain.user.use_case.register import Register
from infraestructure.user.repository.user import User as user_repository

app = Flask(__name__)


@app.route("/")
def welcome():
    return "api working."


@app.route("/user/auth", methods=['POST'])
def login():
    req = request.data.decode('utf-8')
    data = json.loads(req)
    try:
        repository = user_repository()
        user = Login(repository).login(data['email'], data['password'])
        if user is None:
            return ('Not allowed', 401)
        else:
            return ('Logged', 200)
    except Exception as ex:
        return (str(ex), 400)


@app.route("/user/register", methods=['POST'])
def register():
    req = request.data.decode('utf-8')
    data = json.loads(req)
    try:
        repository = user_repository()
        user = Register(repository).register(data['email'], data['password'])
        if user is None:
            return ('Not allowed', 401)
        else:
            return ('Registered', 200)
    except Exception as ex:
        return (str(ex), 400)
