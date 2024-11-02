
# Generative AI Assistant

This project is a **Generative AI Assistant** built using the GPT-2 model. It leverages OpenAI's Transformer architecture to generate text-based responses to user prompts, providing a framework for a simple and customizable text generation API.

## Project Structure

The structure of the project is organized as follows:

```
.
├── .github               # GitHub-specific configurations (e.g., workflows)
├── data
│   └── model             # Directory for storing model and tokenizer files
│       ├── config.json
│       ├── generation_config.json
│       ├── merges.txt
│       ├── model.safetensors
│       ├── special_tokens_map.json
│       ├── tokenizer_config.json
│       ├── tokenizer.json
│       ├── vocab.json
│       └── vocab.txt
├── models                # (Optional) Additional or alternative models can be stored here
├── src                   # Source code for the project
│   ├── __init__.py       # Package initialization
│   ├── api.py            # FastAPI app that provides endpoints for text generation
│   ├── model.py          # Main model class for loading and generating responses
│   └── utils.py          # Utility functions used across the project
├── tests                 # Unit tests for the project
│   ├── __init__.py
│   ├── test_api.py       # Tests for the API endpoints
│   ├── test_model.py     # Tests for the model's functionality
│   └── utils.py          # Additional test utilities if needed
├── venv                  # Virtual environment for Python dependencies
├── .gitignore            # Specifies files and folders to ignore in Git
├── LICENSE               # Project license
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies for the project
└── setup.py              # Setup script for installing the package
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Vitmer/generative-ai-assistant.git
   cd generative-ai-assistant
   ```

2. **Set up a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the GPT-2 model**:

   Run the `download_model.py` script to download the GPT-2 model files to `data/model`:

   ```bash
   python download_model.py
   ```

## Usage

1. **Run the FastAPI server**:

   ```bash
   uvicorn src.api:app --reload
   ```

2. **Access the API documentation**:

   Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to see the interactive Swagger documentation.

3. **Example API call**:

   You can use `curl` to test the `/generate` endpoint:

   ```bash
   curl -X 'POST'      'http://127.0.0.1:8000/generate'      -H 'accept: application/json'      -H 'Content-Type: application/json'      -d '{ "prompt": "What is the meaning of life?" }'
   ```

   The server will respond with a generated answer based on the input prompt.

## Project Components

- **FastAPI**: Provides the web framework for creating API endpoints.
- **Transformers**: Used for loading GPT-2 and generating text responses.
- **Data and Model Files**: The `data/model` folder contains all necessary files for the GPT-2 model and tokenizer.
- **Testing**: Unit tests for the API and model functionality are located in the `tests` folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
