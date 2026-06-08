from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from database import SessionLocal

from models import Base
from models import Patient, Service

from schemas import PatientCreate, ServiceCreate

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

@app.post("/services")
def create_service(service_data: ServiceCreate):

    db: Session = SessionLocal()

    service = Service(
        name=service_data.name,
        price=service_data.price,
        description=service_data.description
    )

    db.add(service)
    db.commit()
    db.refresh(service)

    return service

@app.get("/services")
def get_services():

    db: Session = SessionLocal()

    services = db.query(Service).all()

    return services

@app.delete("/services/{service_id}")
def delete_service(service_id: int):

    db: Session = SessionLocal()

    service = db.query(Service).filter(
        Service.id == service_id
    ).first()

    if not service:
        return {"message": "Service not found"}

    db.delete(service)
    db.commit()

    return {"message": "Deleted"}

@app.put("/services/{service_id}")
def update_service(
    service_id: int,
    service_data: ServiceCreate
):

    db: Session = SessionLocal()

    service = db.query(Service).filter(
        Service.id == service_id
    ).first()

    if not service:
        return {"message": "Service not found"}

    service.name = service_data.name
    service.price = service_data.price
    service.description = service_data.description

    db.commit()

    return {"message": "Updated"}        