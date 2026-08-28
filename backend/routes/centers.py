from fastapi import APIRouter, Depends, status
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
