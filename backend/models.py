from pydantic import BaseModel

class Product (BaseModel):
    # this only declares that thr product object should have these attributes it does not create or initialize them
    id:int
    name:str
    description:str
    price:float
    quantity:int

    