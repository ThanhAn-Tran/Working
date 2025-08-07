from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Pet
from .schemas.pet import PetCreate, PetUpdate, PetStatistics
from typing import Optional, List, Dict, Any

def get_pet(db: Session, pet_id: int) -> Optional[Pet]:
    return db.query(Pet).filter(Pet.id == pet_id).first()

def get_pets(db: Session, skip: int = 0, limit: int = 100) -> List[Pet]:
    return db.query(Pet).offset(skip).limit(limit).all()

def create_pet(db: Session, pet: PetCreate) -> Pet:
    db_pet = Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def update_pet(db: Session, pet_id: int, pet_update: PetUpdate) -> Optional[Pet]:
    db_pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if db_pet:
        update_data = pet_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_pet, field, value)
        db.commit()
        db.refresh(db_pet)
    return db_pet

def delete_pet(db: Session, pet_id: int) -> bool:
    db_pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if db_pet:
        db.delete(db_pet)
        db.commit()
        return True
    return False

def get_pet_statistics(db: Session) -> Dict[str, Any]:
    total_pets = db.query(Pet).count()
    
    # Average weight (only for pets with weight data)
    avg_weight = db.query(func.avg(Pet.weight)).filter(Pet.weight.isnot(None)).scalar()
    
    # Count by type
    type_counts = db.query(Pet.type, func.count(Pet.id)).group_by(Pet.type).all()
    type_distribution = {pet_type: count for pet_type, count in type_counts}
    
    return {
        "total_pets": total_pets,
        "average_weight": round(avg_weight, 2) if avg_weight else None,
        "type_distribution": type_distribution
    }