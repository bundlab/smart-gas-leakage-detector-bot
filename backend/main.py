from fastapi import FastAPI
from database import SessionLocal
from models import GasReading
from telegram_bot import send_alert
from config import GAS_THRESHOLD

app = FastAPI()

@app.post("/api/gas")
def receive_gas(data: dict):
    level = data.get("gas_level")
    db = SessionLocal()
    db.add(GasReading(gas_level=level))
    db.commit()

    if level > GAS_THRESHOLD:
        send_alert(level)

    return {"status": "ok"}