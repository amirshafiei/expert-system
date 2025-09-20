import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_rules():
    response = client.get("/rules")
    assert response.status_code == 200
    data = response.json()
    assert "rules" in data
    assert len(data["rules"]) > 0
    assert "id" in data["rules"][0]
    assert "if" in data["rules"][0]
    assert "then" in data["rules"][0]

def test_diagnose_with_symptoms():
    response = client.post("/diagnose", json={
        "symptoms": ["تب بالا", "سردرد", "بدن درد"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "conclusions" in data
    assert "احتمال آنفولانزا" in data["conclusions"]

def test_diagnose_no_symptoms():
    response = client.post("/diagnose", json={"symptoms": []})
    assert response.status_code == 200
    data = response.json()
    assert "conclusions" in data