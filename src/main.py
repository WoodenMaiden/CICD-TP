"""
Main module
"""

import os
import prometheus_client as prom
from flask import Flask
from flask import request

from city import City
from db import Database

app = Flask(__name__)

db = Database()
db.create_city_table()

duration = prom.Summary("duration_seconds", "Duration of requests in seconds")
get_req = prom.Counter("nb_queries", "number of GET queries")


@app.route("/metrics")
def metrics():
    """Endpoint used by prometeus"""
    return prom.generate_latest(), 200


@duration.time()
@app.route("/city", methods=["GET"])
def get_city():
    """Endpoint to get all cities"""
    get_req.inc()
    return {"cities": [city.get_dict() for city in db.get_cities()]}, 200


@duration.time()
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


@app.route("/")
def routes():
    """Routes listing endpoint"""
    return (
        "Welcome to the City API.<br />"
        "Available endpoints:<br />"
        "  POST /city<br />"
        "  GET /city<br />"
        "  GET /_health<br />"
        "  GET /metrics<br />"
    )


if __name__ == "__main__":
    app.run(
        host=os.environ.get("CITY_API_ADDR", "0.0.0.0"),
        port=int(os.environ.get("CITY_API_PORT", 5000)),
        debug=True,
    )
