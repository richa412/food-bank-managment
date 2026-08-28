from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import database_models
from database import get_db
from schemas import CenterCreate, CenterResponse


router = APIRouter(prefix="/centers", tags=["centers"])


@router.get("", response_model=list[CenterResponse])
def get_centers(db: Session = Depends(get_db)):
    return db.query(database_models.DistributionCenter).all()


@router.post("", response_model=CenterResponse, status_code=status.HTTP_201_CREATED)
def create_center(center: CenterCreate, db: Session = Depends(get_db)):
    db_center = database_models.DistributionCenter(**center.model_dump())
    db.add(db_center)
    db.commit()
    db.refresh(db_center)
    return db_center


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_center(id: int, db: Session = Depends(get_db)):
    db_center = (
        db.query(database_models.DistributionCenter)
        .filter(database_models.DistributionCenter.id == id)
        .first()
    )
    if db_center is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Distribution center not found")

    db.delete(db_center)
    db.commit()
