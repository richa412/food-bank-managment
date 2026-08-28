from datetime import date

from pydantic import BaseModel


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
