import os
from transformers import AutoTokenizer, AutoModelForCausalLM

class GenerativeModel:
    def __init__(self, model_path="./data/model"):
        """
        Initializes the GenerativeModel with a specified model path.
        
        Parameters:
        - model_path (str): Path to the directory where the model and tokenizer are saved.
        
        Raises:
        - FileNotFoundError: If the specified model path does not exist.
        """
        # Check if the model directory exists
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"The model directory '{model_path}' does not exist. "
                "Please download the model by running `download_model.py`."
            )
        
        # Load tokenizer and model from the specified path
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)
        print("Model and tokenizer loaded successfully from", model_path)

    def generate_answer(self, prompt, max_length=100):
        """
        Generates an answer based on the given prompt using the loaded model.
        
        Parameters:
        - prompt (str): The input text for the model to generate a response.
        - max_length (int): The maximum length of the generated response.
        
        Returns:
        - str: The generated response.
        """
        # Tokenize input prompt
        inputs = self.tokenizer(prompt, return_tensors="pt")
        
        # Generate response with specified parameters for diversity and length control
        outputs = self.model.generate(
            inputs["input_ids"], 
            max_length=max_length, 
            num_return_sequences=1,
            no_repeat_ngram_size=2,  # Avoids repeating the same phrases
            top_k=40,                # Chooses from the top 40 tokens
            top_p=0.8,               # Uses nucleus sampling for diversity
            temperature=0.5          # Controls creativity of the model
        )
        
        # Decode the generated response and remove special tokens
        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return answer