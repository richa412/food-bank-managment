from datetime import date, datetime

from pydantic import BaseModel, Field


class FoodBase(BaseModel):
    name: str
    category: str
    quantity: int
    unit: str
    expiry_date: date
    donor: str


class FoodCreate(FoodBase):
    pass


class FoodUpdate(FoodBase):
    pass


class FoodResponse(FoodBase):
    id: int

    model_config = {"from_attributes": True}


class CenterCreate(BaseModel):
    name: str


class CenterResponse(CenterCreate):
    id: int

    model_config = {"from_attributes": True}


class DistributionCreate(BaseModel):
    food_id: int
    center_id: int
    quantity: int = Field(gt=0)


class DistributionResponse(DistributionCreate):
    id: int
    distributed_at: datetime

    model_config = {"from_attributes": True}
