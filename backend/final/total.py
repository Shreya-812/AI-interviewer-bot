from fastapi import FastAPI, Request
from pydantic import BaseModel
import os
import openai

from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize app
app = FastAPI()

# Prompt map for prompt type to file path
PROMPT_MAP = {
    "hr": "prompts/hr_prompt.txt",
    "tech": "prompts/tech_prompt.txt",
    "stress": "prompts/stress_prompt.txt"
}

# Data models
class AskRequest(BaseModel):
    prompt_type: str
    question: str

class ScoreRequest(BaseModel):
    answer: str

# Utility: Call OpenAI API
def query_llm(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()

# Utility: Load prompt from file
def load_prompt(prompt_type: str) -> str:
    path = PROMPT_MAP.get(prompt_type)
    if not path or not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        return f.read()

# Utility: Simple rubric scoring
def evaluate_answer(answer: str) -> int:
    if len(answer.strip()) == 0:
        return 0
    elif "confident" in answer.lower():
        return 8
    elif "teamwork" in answer.lower():
        return 7
    else:
        return 5

# Routes
@app.get("/")
def root():
    return {"message": "AI Interviewer Chatbot Backend Running"}

@app.post("/ask")
async def ask(request: AskRequest):
    base_prompt = load_prompt(request.prompt_type)
    if not base_prompt:
        return {"error": "Invalid prompt type"}
    full_prompt = f"{base_prompt}\n\nQuestion: {request.question}"
    answer = query_llm(full_prompt)
    return {"response": answer}

@app.post("/score")
async def score(request: ScoreRequest):
    score = evaluate_answer(request.answer)
    return {"score": score}
