from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import EmailStr
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from schemas import Message, InterviewRequest, InterviewFeedback
from utils import evaluate_response, generate_feedback

app = FastAPI()

# CORS setup for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Interview Bot Backend Running"}

@app.post("/contact")
def handle_contact(msg: Message):
    print(f"Received message from {msg.name} ({msg.email}): {msg.message}")
    return {"message": "Your message has been received!"}

@app.post("/score", response_model=list[InterviewFeedback])
def score_interview(data: InterviewRequest):
    print(f"Evaluating interview for role: {data.role}")
    feedback = []
    for ans in data.responses:
        score = evaluate_response(ans.answer)
        fb = generate_feedback(ans.answer)
        feedback.append(InterviewFeedback(
            question=ans.question,
            score=score,
            feedback=fb
        ))
    return feedback
