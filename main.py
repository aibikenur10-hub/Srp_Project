from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, Base, get_db
import models
from services.oylan import send_message
from services.chat import save_message, get_history

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


class ChatRequest(BaseModel):
    message: str
    session_id: str = 'default'


class AnalyzeRequest(BaseModel):
    region: str
    risk_type: str
    language: str = "ru"


@app.get('/')
def root():
    return {'message': 'ClimateGuard assistant is running!'}


@app.get('/health')
def health():
    return {'status': 'ok'}


@app.post('/chat')
async def chat(req: ChatRequest, db: AsyncSession = Depends(get_db)):
    if not req.message.strip():
        raise HTTPException(400, detail='Message cannot be empty')
    try:
        history = await get_history(db, req.session_id)
        reply = await send_message(req.message, history)
        await save_message(db, req.session_id, 'user', req.message)
        await save_message(db, req.session_id, 'assistant', reply)
        return {'reply': reply, 'session_id': req.session_id}
    except Exception as e:
        raise HTTPException(500, detail=str(e))


@app.get('/history/{session_id}')
async def history(session_id: str, db: AsyncSession = Depends(get_db)):
    msgs = await get_history(db, session_id, limit=50)
    return {'session_id': session_id, 'messages': msgs}


@app.post("/analyze")
async def analyze(req: AnalyzeRequest, db: AsyncSession = Depends(get_db)):
    lang_map = {"ru": "Russian", "kz": "Kazakh", "en": "English"}
    lang = lang_map.get(req.language, "Russian")
    risk_map = {"flood": "flood risk (паводок)", "drought": "drought risk (засуха)"}
    risk = risk_map.get(req.risk_type, req.risk_type)
    prompt = f"Analyze the {risk} for {req.region} region of Kazakhstan. Respond in {lang}."
    session_id = f"analyze-{req.region}-{req.risk_type}"
    try:
        history = await get_history(db, session_id)
        reply = await send_message(prompt, history)
        await save_message(db, session_id, 'user', prompt)
        await save_message(db, session_id, 'assistant', reply)
        return {"analysis": reply, "region": req.region, "risk_type": req.risk_type}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
