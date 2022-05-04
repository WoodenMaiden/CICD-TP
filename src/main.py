from flask import Flask
from flask import request

from city import City
from db import Database

app = Flask(__name__)

db = Database()
db.create_city_table()

@app.route('/city', methods=['GET'])
def get_city():
    return { 'cities': [city.get_dict() for city in db.get_cities()] }, 200

@app.route('/city', methods=['POST'])
def post_city():
    body = request.get_json()
    db.post_city(City(**body))
    return '', 201

@app.route('/_health', methods=['GET'])
def health():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)