from flask import Flask
from flask import request

from city import City
from db import connect, get_cities, post_city

app = Flask(__name__)

connection = connect()

@app.route('/city', methods=['GET'])
async def get_city():
    return await get_cities(connection)

@app.route('/city', methods=['POST'])
async def post_city():
    body = request.get_json()

    return await post_city(connection, City(**body))

@app.route('/_health', methods=['GET'])
def health():
    return 204