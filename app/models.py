from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from .database import Base


class Pet(Base):
    __tablename__ = "pet_name_weight_type"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    type = Column(String, index=True, nullable=False) 
    weight = Column(Float, nullable=True)
