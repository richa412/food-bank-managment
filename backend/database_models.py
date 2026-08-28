from sqlalchemy import Column, Date, DateTime, Integer, String
from sqlalchemy.sql import func
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


class Distribution(Base):
    __tablename__ = "distributions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    food_id = Column(Integer, nullable=False)
    center_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    distributed_at = Column(DateTime, nullable=False, server_default=func.now())
