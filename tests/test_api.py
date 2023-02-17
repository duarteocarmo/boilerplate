from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


class TestAPI:
    def test_read_root(self):
        response = client.get("/")
        assert response.status_code == 200

    def test_read_hello(self):
        response = client.post("/hello")
        assert response.status_code == 200
        assert "We are here" in response.text
