import random

def evaluate_response(response: str) -> int:
    return random.randint(2, 5)  # Random score for demo

def generate_feedback(answer: str) -> str:
    return "Good attempt. Try to elaborate more next time."
