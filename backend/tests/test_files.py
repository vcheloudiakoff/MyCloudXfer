# tests/test_files.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_permanent_file():
    response = client.post("/permanent-files/", json={
        "filename": "test_file.txt",
        "file_path": "/path/to/file",
        "folder_id": None
    })
    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == "test_file.txt"
    assert "id" in data
