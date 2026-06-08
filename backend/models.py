from sqlalchemy import Column, Integer, String

from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String)
    phone = Column(String)
    gender = Column(String)

    dob = Column(String)
    address = Column(String)