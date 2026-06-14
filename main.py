from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"message": "ClimateGuard assistant is running!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest):
    # placeholder echo — real Oylan API connection comes in the next lesson
    return {"reply": f"You said: {req.message}"}
