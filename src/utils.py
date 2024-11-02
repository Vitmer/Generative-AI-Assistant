import logging

def setup_logging():
    # Configure logging settings
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

def normalize_text(text):
    """Simple function to normalize text."""
    return text.lower().strip()