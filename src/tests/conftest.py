"""config for tests"""
import pytest
from main import app as flask_app


@pytest.fixture()
def app():
    """init app"""

    flask_app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield flask_app

    # clean up / reset resources here


@pytest.fixture()
def client(city_app):
    """client"""
    return city_app.test_client()


@pytest.fixture()
def runner(city_app):
    """runner"""
    return city_app.test_cli_runner()
