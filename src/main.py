"""
Main module
"""

import os
from flask import Flask
from flask import request

from city import City
from db import Database

app = Flask(__name__)

db = Database()
db.create_city_table()


@app.route("/city", methods=["GET"])
def get_city():
    """Endpoint to get all cities"""
    return {"cities": [city.get_dict() for city in db.get_cities()]}, 200


@app.route("/city", methods=["POST"])
def post_city():
    """Endpoint to create a new city"""
    body = request.get_json()
    db.post_city(City(**body))
    return "", 201


@app.route("/_health", methods=["GET"])
def health():
    """Health check endpoint"""
    return "", 204


if __name__ == "__main__":
    app.run(
        host=os.environ.get("CITY_API_ADDR", "localhost"),
        port=int(os.environ.get("CITY_API_PORT", 5000)),
        debug=True,
    )
