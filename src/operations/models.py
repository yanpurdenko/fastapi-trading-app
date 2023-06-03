from sqlalchemy import Column, Integer, String, TIMESTAMP

from src.database import Base


class Operation(Base):
    __tablename__ = "operation"

    id = Column(Integer, primary_key=True)
    quantity = Column(String(length=255))
    figi = Column(String(length=255))
    instrument_type = Column(String(length=255), nullable=True)
    date = Column(TIMESTAMP)
    type = Column(String(length=255))
