from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class GasReading(Base):
    __tablename__ = "gas_readings"
    id = Column(Integer, primary_key=True)
    gas_level = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)