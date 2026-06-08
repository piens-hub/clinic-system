from pydantic import BaseModel

class PatientCreate(BaseModel):
    full_name: str
    phone: str
    gender: str

    dob: str
    address: str