from sqlalchemy import Column, Integer, String, Boolean

from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String)
    phone = Column(String)
    gender = Column(String)

    dob = Column(String)
    address = Column(String)

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    price = Column(Integer, nullable=False)

    description = Column(String, default="")

    is_active = Column(Boolean, default=True)