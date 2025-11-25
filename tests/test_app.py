import pytest
from app import app as flask_app


def test_index():
    client = flask_app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b'Simple Webapp' in res.data


def test_health():
    client = flask_app.test_client()
    res = client.get('/api/health')
    assert res.status_code == 200
    assert res.get_json() == {'status': 'ok'}
