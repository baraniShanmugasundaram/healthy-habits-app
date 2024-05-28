import sys
import os
import pytest
from app import create_app
from app.models import db, Habit

# Ensure the app module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

def test_index(client):
    rv = client.get('/')
    assert b'Healthy Habits Tracker' in rv.data
