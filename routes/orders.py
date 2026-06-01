from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Order, OrderItem, Product, Customer
from schemas import OrderCreate, OrderResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    # Check customer exists
    customer = db.query(Customer).filter(
        Customer.id == order.customer_id
    ).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    # Validate all products and stock
    total_amount = 0.0
    order_items = []
    
    for item in order.items:
        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()
        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Product {item.product_id} not found"
            )
        
        # Check sufficient stock
        if product.quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for {product.name}. Available: {product.quantity}"
            )
        
        total_amount += product.price * item.quantity
        order_items.append({
            "product": product,
            "quantity": item.quantity,
            "unit_price": product.price
        })
    
    # Create order
    db_order = Order(
        customer_id=order.customer_id,
        total_amount=total_amount
    )
    db.add(db_order)
    db.flush()
    
    # Create order items and reduce stock
    for item_data in order_items:
        db_item = OrderItem(
            order_id=db_order.id,
            product_id=item_data["product"].id,
            quantity=item_data["quantity"],
            unit_price=item_data["unit_price"]
        )
        db.add(db_item)
        
        # Reduce stock automatically
        item_data["product"].quantity -= item_data["quantity"]
    
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get("/{id}", response_model=OrderResponse)
def get_order(id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/{id}")
def delete_order(id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Restore stock when order is cancelled
    for item in order.items:
        product = db.query(Product).filter(
            Product.id == item.product_id
        ).first()
        if product:
            product.quantity += item.quantity
    
    db.delete(order)
    db.commit()
    return {"message": "Order cancelled successfully"}
