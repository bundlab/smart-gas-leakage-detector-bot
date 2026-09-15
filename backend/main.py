from fastapi import FastAPI
from backend.database import SessionLocal, engine
from backend.models import Base, GasReading
from backend.telegram_bot import send_alert
from backend.config import GAS_THRESHOLD

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Smart Gas Leakage Detector Bot API",
        "status": "running"
    }


@app.post("/api/gas")
def receive_gas(data: dict):
    level = data.get("gas_level")

    db = SessionLocal()

    try:
        db.add(GasReading(gas_level=level))
        db.commit()

        if level > GAS_THRESHOLD:
            send_alert(level)

        return {"status": "ok"}

    finally:
        db.close()