from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import database_models
from database import get_db
from schemas import FoodCreate, FoodResponse, FoodUpdate


router = APIRouter(prefix="/foods", tags=["foods"])


@router.get("", response_model=list[FoodResponse])
def get_foods(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()


@router.post("", response_model=FoodResponse, status_code=status.HTTP_201_CREATED)
def create_food(food: FoodCreate, db: Session = Depends(get_db)):
    db_food = database_models.Product(**food.model_dump())
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food


@router.put("/{id}", response_model=FoodResponse)
def update_food(id: int, food: FoodUpdate, db: Session = Depends(get_db)):
    db_food = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_food is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food not found")

    for field, value in food.model_dump().items():
        setattr(db_food, field, value)

    db.commit()
    db.refresh(db_food)
    return db_food


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_food(id: int, db: Session = Depends(get_db)):
    db_food = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_food is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food not found")

    db.delete(db_food)
    db.commit()
