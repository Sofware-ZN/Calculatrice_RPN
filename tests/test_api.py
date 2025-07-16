import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_stack():
    response = client.post("/rpn/stack")
    assert response.status_code == 200
    assert "stack_id" in response.json()
