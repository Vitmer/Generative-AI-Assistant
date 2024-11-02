import unittest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

class TestAPI(unittest.TestCase):

    def test_generate_endpoint(self):
        # Test that the /generate endpoint returns a 200 status code
        response = client.post("/generate", json={"prompt": "What is the capital of France?"})
        self.assertEqual(response.status_code, 200)
        
        # Check that the response contains the expected fields
        data = response.json()
        self.assertIn("prompt", data)
        self.assertIn("answer", data)
        self.assertEqual(data["prompt"], "What is the capital of France?")
        self.assertIsInstance(data["answer"], str)
        self.assertGreater(len(data["answer"]), 0)

if __name__ == "__main__":
    unittest.main()