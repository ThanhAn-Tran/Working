from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List
from ..database import SessionLocal, engine
from ..models import Pet
from ..schemas.pet import Pet as PetSchema, PetCreate, PetUpdate, PetStatistics
from ..crud import get_pets, get_pet, create_pet, update_pet, delete_pet, get_pet_statistics

# Create tables
Pet.metadata.create_all(bind=engine)

router = APIRouter(prefix="/pets", tags=["pets"])


# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[PetSchema])
def get_pets_endpoint(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    db: Session = Depends(get_db)
):
    """Get list of pets with pagination"""
    pets = get_pets(db, skip=skip, limit=limit)
    return pets


@router.get("/statistics", response_model=PetStatistics)
def get_pet_statistics_endpoint(db: Session = Depends(get_db)):
    """Get pet statistics including total count, average weight, and type distribution"""
    return get_pet_statistics(db)


@router.get("/{pet_id}", response_model=PetSchema)
def get_pet_endpoint(pet_id: int, db: Session = Depends(get_db)):
    """Get a specific pet by ID"""
    pet = get_pet(db, pet_id=pet_id)
    if pet is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pet with id {pet_id} not found"
        )
    return pet


@router.post("/", response_model=PetSchema, status_code=status.HTTP_201_CREATED)
def create_pet_endpoint(pet: PetCreate, db: Session = Depends(get_db)):
    """Create a new pet"""
    return create_pet(db=db, pet=pet)


@router.put("/{pet_id}", response_model=PetSchema)
def update_pet_endpoint(pet_id: int, pet_update: PetUpdate, db: Session = Depends(get_db)):
    """Update a pet completely"""
    updated_pet = update_pet(db=db, pet_id=pet_id, pet_update=pet_update)
    if updated_pet is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pet with id {pet_id} not found"
        )
    return updated_pet


@router.patch("/{pet_id}", response_model=PetSchema)
def patch_pet_endpoint(pet_id: int, pet_update: PetUpdate, db: Session = Depends(get_db)):
    """Partially update a pet"""
    updated_pet = update_pet(db=db, pet_id=pet_id, pet_update=pet_update)
    if updated_pet is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pet with id {pet_id} not found"
        )
    return updated_pet


@router.delete("/{pet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pet_endpoint(pet_id: int, db: Session = Depends(get_db)):
    """Delete a pet"""
    success = delete_pet(db=db, pet_id=pet_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pet with id {pet_id} not found"
        )
    return None
