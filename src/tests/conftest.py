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


# pylint: disable=redefined-outer-name
@pytest.fixture()
def client(app):
    """client"""
    return app.test_client()


# pylint: disable=redefined-outer-name
@pytest.fixture()
def runner(app):
    """runner"""
    return app.test_cli_runner()
