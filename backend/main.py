from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from database import SessionLocal

from models import Base
from models import Patient

from schemas import PatientCreate

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Clinic System"}

@app.post("/patients")
def create_patient(patient: PatientCreate):

    db: Session = SessionLocal()

    new_patient = Patient(
    full_name=patient.full_name,
    phone=patient.phone,
    gender=patient.gender,
    dob=patient.dob,
    address=patient.address
)

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {
        "id": new_patient.id,
        "full_name": new_patient.full_name
    }
@app.get("/patients")
def get_patients():

    db: Session = SessionLocal()

    patients = db.query(Patient).all()

    return patients
@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):

    db: Session = SessionLocal()

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        return {"message": "Patient not found"}

    db.delete(patient)
    db.commit()

    return {"message": "Deleted"}
@app.put("/patients/{patient_id}")
def update_patient(
    patient_id: int,
    patient_data: PatientCreate
):

    db: Session = SessionLocal()

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        return {"message": "Patient not found"}

    patient.full_name = patient_data.full_name
    patient.phone = patient_data.phone
    patient.gender = patient_data.gender
    patient.dob = patient_data.dob
    patient.address = patient_data.address

    db.commit()

    return {"message": "Updated"}