from pydantic import BaseModel, EmailStr
from typing import List

class Message(BaseModel):
    name: str
    email: EmailStr
    message: str

class Answer(BaseModel):
    question: str
    answer: str

class InterviewRequest(BaseModel):
    role: str
    responses: List[Answer]

class InterviewFeedback(BaseModel):
    question: str
    score: int
    feedback: str
