from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Product (Base):
    __tablename__ = "product"
    id =Column(Integer,primary_key = True, index = True)
    name =Column(String)
    category = Column(String)
    quantity=Column(Integer)
    unit = Column(String)
    expiry_date = Column(Date)
    donor = Column(String)


class DistributionCenter(Base):
    __tablename__ = "distribution_centers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
