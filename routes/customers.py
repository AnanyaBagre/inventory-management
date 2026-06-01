from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Customer
from schemas import CustomerCreate, CustomerResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    # Check email uniqueness
    existing = db.query(Customer).filter(
        Customer.email == customer.email
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    db_customer = Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.get("/", response_model=List[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

@router.get("/{id}", response_model=CustomerResponse)
def get_customer(id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.delete("/{id}")
def delete_customer(id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    db.delete(customer)
    db.commit()
    return {"message": "Customer deleted successfully"}
