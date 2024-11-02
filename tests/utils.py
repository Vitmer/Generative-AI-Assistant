import unittest
from src.utils import setup_logging, normalize_text

class TestUtils(unittest.TestCase):
    
    def test_setup_logging(self):
        # Test that logger is created and works as expected
        logger = setup_logging()
        self.assertIsNotNone(logger)
        logger.info("This is a test log message")

    def test_normalize_text(self):
        # Test that normalize_text correctly normalizes input
        text = "  Hello World!  "
        normalized_text = normalize_text(text)
        self.assertEqual(normalized_text, "hello world!")

if __name__ == "__main__":
    unittest.main()