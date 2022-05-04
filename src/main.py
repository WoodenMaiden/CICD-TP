from flask import Flask
from flask import request

from city import City
from db import Database

app = Flask(__name__)

db = Database()

@app.route('/city', methods=['GET'])
def get_city():
    return db.get_cities()

@app.route('/city', methods=['POST'])
def post_city():
    body = request.get_json()
    print(body)

    return db.post_city(City(**body))

@app.route('/_health', methods=['GET'])
def health():
    return 204

if __name__ == '__main__':
    app.run(debug=True)