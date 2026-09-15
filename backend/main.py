from fastapi import FastAPI
from backend.database import SessionLocal
from backend.models import GasReading
from backend.telegram_bot import send_alert
from backend.config import GAS_THRESHOLD

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