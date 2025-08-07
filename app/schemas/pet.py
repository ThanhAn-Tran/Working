from pydantic import BaseModel, ConfigDict
from typing import Optional


class PetBase(BaseModel):
    name: str
    type: str
    weight: Optional[float] = None


class PetCreate(PetBase):
    pass


class PetUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    weight: Optional[float] = None


class Pet(PetBase):
    id: int
    # Allow reading SQLAlchemy model attributes directly
    model_config = ConfigDict(from_attributes=True)


class PetStatistics(BaseModel):
    total_pets: int
    average_weight: Optional[float]
    type_distribution: dict[str, int]
