import os
import tempfile

import pytest

import hello


@pytest.fixture
def client():
    hello.app.config['TESTING'] = True
    client = hello.app.test_client()
    yield client


# Unit test
def test_hello_world(client):
    """Test if index has hello world."""

    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Hello World' in rv.data

# Regression
def test_admin_name_is_not_reveled(client):
    response = client.post('/admin')
    assert response.status_code == 404

# Assert we get same number with /num api
def test_same_num_with_num(client):
    rv = client.get('/num?num=44')
    assert rv.json["num"] == "144"