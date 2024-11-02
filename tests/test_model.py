import unittest
from src.model import GenerativeModel

class TestGenerativeModel(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Initialize the model once for all tests
        cls.model = GenerativeModel(model_name="gpt-2")

    def test_model_loads(self):
        # Test that model loads correctly
        self.assertIsNotNone(self.model.model)
        self.assertIsNotNone(self.model.tokenizer)

    def test_generate_answer(self):
        # Test that the model can generate an answer
        prompt = "What is the meaning of life?"
        answer = self.model.generate_answer(prompt)
        self.assertIsInstance(answer, str)
        self.assertGreater(len(answer), 0)

if __name__ == "__main__":
    unittest.main()