# Inventory Management System

A FastAPI-based Inventory Management System that provides APIs for managing products, customers, and orders.

## Project Structure

inventory-management/
└── backend/
├── routes/
│   ├── **init**.py
│   ├── customers.py
│   ├── orders.py
│   └── products.py
├── .env
├── Dockerfile
├── database.py
├── main.py
├── models.py
├── schemas.py
└── requirements.txt

## Installation

```bash
cd backend
pip install -r requirements.txt
```

## Run Application

```bash
uvicorn main:app --reload
```

## API Documentation

After starting the server:

http://localhost:8000/docs

## Features

* Product Management
* Customer Management
* Order Management
* FastAPI Backend
* Database Integration
* Docker Support
