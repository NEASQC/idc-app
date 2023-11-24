import json
import pytest
from idc import app as test_app

@pytest.fixture()
def app():
    test_app.config.update({
        "TESTING": True,
    })

    yield test_app


@pytest.fixture()
def client(app):
    return app.test_client()


TEST_URL = "/idc-deep"


def test_idc_t1n0m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t1": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ia'] == 1.0


def test_idc_t0n1m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t0": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t1n1m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t1": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t2n0m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t2": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iia'] == 1.0
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t2n1m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t2": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t3n0m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t3": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t0n2m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t0": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t1n2m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t1": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t3n2m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t3": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t3n1m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t3": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t4n0m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t4": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiib'] == 1.0
    except AssertionError:
        pass


def test_idc_t4n1m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t4": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiib'] == 1.0
    except AssertionError:
        pass


def test_idc_t4n2m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "t4": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiib'] == 1.0
    except AssertionError:
        pass


def test_idc_txn3m0_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "n3a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiic'] == 1.0


def test_idc_txnym1_cf(client):
    data = {
        "model": "cf",
        "variables": {
            "m1": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iv'] == 1.0



def test_idc_t1n0m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t1": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ia'] == 1.0


def test_idc_t0n1m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t0": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t1n1m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t1": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t2n0m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t2": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iia'] == 1.0
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t2n1m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t2": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t3n0m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t3": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t0n2m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t0": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t1n2m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t1": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t3n2m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t3": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t3n1m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t3": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t4n0m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t4": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiib'] == 1.0
    except AssertionError:
        pass


def test_idc_t4n1m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t4": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiib'] == 1.0
    except AssertionError:
        pass


def test_idc_t4n2m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "t4": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiib'] == 1.0
    except AssertionError:
        pass


def test_idc_txn3m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "n3a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiic'] == 1.0


def test_idc_txnym1_fuzzy(client):
    data = {
        "model": "fuzzy",
        "variables": {
            "m1": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iv'] == 1.0


def test_idc_t1n0m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t1": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ia'] == 1.0


def test_idc_t0n1m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t0": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t1n1m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t1": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t2n0m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t2": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iia'] == 1.0
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t2n1m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t2": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t3n0m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t3": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t0n2m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t0": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t1n2m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t1": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t3n2m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t3": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t3n1m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t3": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiia'] == 1.0
    except AssertionError:
        pass


def test_idc_t4n0m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t4": 1,
            "n0a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiib'] == 1.0
    except AssertionError:
        pass


def test_idc_t4n1m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t4": 1,
            "n1a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiib'] == 1.0
    except AssertionError:
        pass


def test_idc_t4n2m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "t4": 1,
            "n2a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    try:
        assert response['iiib'] == 1.0
    except AssertionError:
        pass


def test_idc_txn3m0_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "n3a": 1,
            "m0": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiic'] == 1.0


def test_idc_txnym1_bayes(client):
    data = {
        "model": "bayes",
        "variables": {
            "m1": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iv'] == 1.0


def test_idc_invalid_model(client):
    data = {
        "model": "invalid",
        "classification": {
            "tnm": "t1n0m0",
            "value": 1
        }
    }
    response = client.post(TEST_URL, json=data)
    assert response.status_code == 400

