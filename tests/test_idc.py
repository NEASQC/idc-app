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


TEST_URL = "/idc"


def test_idc_t1n0m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t1n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ia'] == 1.0


def test_idc_t0n1m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t0n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t1n1m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t1n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t2n0m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t2n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iia'] == 1.0
    assert response['iiia'] == 1.0


def test_idc_t2n1m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t2n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t3n0m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t3n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t0n2m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t0n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t1n2m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t1n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t3n2m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t3n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t3n1m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t3n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t4n0m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t4n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiib'] == 1.0


def test_idc_t4n1m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t4n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiib'] == 1.0


def test_idc_t4n2m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "t4n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiib'] == 1.0


def test_idc_txn3m0_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "txn3m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiic'] == 1.0


def test_idc_txnym1_cf(client):
    data = {
        "model": "cf",
        "classification": {
            "tnm": "txnym1",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iv'] == 1.0




def test_idc_t1n0m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t1n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ia'] == 1.0


def test_idc_t0n1m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t0n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t1n1m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t1n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t2n0m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t2n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iia'] == 1.0
    assert response['iiia'] == 1.0


def test_idc_t2n1m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t2n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t3n0m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t3n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t0n2m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t0n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t1n2m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t1n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t3n2m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t3n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t3n1m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t3n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t4n0m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t4n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiib'] == 1.0


def test_idc_t4n1m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t4n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiib'] == 1.0


def test_idc_t4n2m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "t4n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiib'] == 1.0


def test_idc_txn3m0_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "txn3m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiic'] == 1.0


def test_idc_txnym1_fuzzy(client):
    data = {
        "model": "fuzzy",
        "classification": {
            "tnm": "txnym1",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iv'] == 1.0




def test_idc_t1n0m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t1n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ia'] == 1.0


def test_idc_t0n1m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t0n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t1n1m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t1n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['ib'] == 1.0
    assert response['iia'] == 1.0


def test_idc_t2n0m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t2n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iia'] == 1.0
    assert response['iiia'] == 1.0


def test_idc_t2n1m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t2n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t3n0m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t3n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iib'] == 1.0


def test_idc_t0n2m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t0n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t1n2m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t1n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t3n2m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t3n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t3n1m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t3n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiia'] == 1.0


def test_idc_t4n0m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t4n0m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiib'] == 1.0


def test_idc_t4n1m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t4n1m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiib'] == 1.0


def test_idc_t4n2m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "t4n2m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiib'] == 1.0


def test_idc_txn3m0_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "txn3m0",
            "value": 1
        }
    }
    response = json.loads(client.post(TEST_URL, json=data).data)
    assert response['iiic'] == 1.0


def test_idc_txnym1_bayes(client):
    data = {
        "model": "bayes",
        "classification": {
            "tnm": "txnym1",
            "value": 1
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

