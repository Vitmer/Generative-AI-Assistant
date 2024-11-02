from setuptools import setup, find_packages

setup(
    name="advanced-llm-assistant",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "fastapi",
        "uvicorn",
    ],
    entry_points={
        "console_scripts": [
            "run-api=src.api:app",  # Command to run the API
        ],
    },
    author="Your Name",
    description="Advanced LLM Assistant with Generative AI",
    license="MIT",
)