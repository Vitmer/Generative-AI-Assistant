from fastapi import FastAPI
from pydantic import BaseModel
from src.model import GenerativeModel

app = FastAPI()
model = GenerativeModel()

class QueryRequest(BaseModel):
    prompt: str

class QueryResponse(BaseModel):
    prompt: str
    answer: str

@app.post("/generate", response_model=QueryResponse)
async def generate_text(request: QueryRequest):
    # Generate an answer based on the prompt
    answer = model.generate_answer(request.prompt)
    return QueryResponse(prompt=request.prompt, answer=answer)