from sqlalchemy import Column, Integer, String, Float, Date
from database import Base


class InsuranceRate(Base):
    __tablename__ = 'insurance_rate'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    cargo_type = Column(String, index=True)
    rate = Column(Float)
