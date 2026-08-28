from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import database_models
from database import get_db
from schemas import DistributionCreate, DistributionResponse


router = APIRouter(prefix="/distributions", tags=["distributions"])


@router.get("", response_model=list[DistributionResponse])
def get_distributions(db: Session = Depends(get_db)):
    return db.query(database_models.Distribution).all()


@router.post("", response_model=DistributionResponse, status_code=status.HTTP_201_CREATED)
def create_distribution(distribution: DistributionCreate, db: Session = Depends(get_db)):
    food = db.query(database_models.Product).filter(database_models.Product.id == distribution.food_id).first()
    if food is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food not found")

    center = (
        db.query(database_models.DistributionCenter)
        .filter(database_models.DistributionCenter.id == distribution.center_id)
        .first()
    )
    if center is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Distribution center not found")

    if distribution.quantity > food.quantity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient food quantity")

    food.quantity -= distribution.quantity
    db_distribution = database_models.Distribution(
        food_id=distribution.food_id,
        center_id=distribution.center_id,
        quantity=distribution.quantity,
    )
    db.add(db_distribution)
    db.commit()
    db.refresh(db_distribution)
    return db_distribution
