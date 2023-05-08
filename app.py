from flask import Flask
from flask_restful import Api, request
from model import WeaponsStore
import json

app = Flask(__name__)
api = Api(app)


@app.get('/index')
def index():
    return WeaponsStore.index()

@app.post('/add')
def add_weapon():
    data = request.get_json()
    return WeaponsStore.add_weapon(data['name'], data['points'])


if __name__ == '__main__':
    app.run(debug=True)