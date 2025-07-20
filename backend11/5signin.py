@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    from backend11.models import fake_users
    user = fake_users.get(username)
    if user and user["password"] == password:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
