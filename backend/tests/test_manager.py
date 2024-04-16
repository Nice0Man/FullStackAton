from unittest import TestCase
from fastapi.testclient import TestClient

from backend.src.api.v1 import app


class TestHelloWorldEndpoint(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, World!"})
