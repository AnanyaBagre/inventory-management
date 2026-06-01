# Inventory Management System

A full-stack Inventory Management System built with FastAPI, React, PostgreSQL, and Docker.

## Features

* Product Management
* Customer Management
* Order Management
* RESTful API using FastAPI
* React Frontend
* PostgreSQL Database
* Dockerized Deployment
* API Documentation with Swagger UI

---

## Project Structure

```text
inventory-management/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
│   ├── routes/
│   │   ├── products.py
│   │   ├── customers.py
│   │   └── orders.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   ├── package.json
│   ├── Dockerfile
│   └── .env
│
├── docker-compose.yml
└── README.md
```

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Uvicorn

### Frontend

* React
* React Router
* Axios
* Vite

### DevOps

* Docker
* Docker Compose
* GitHub
* Render
* Vercel

---

## Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend server:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

API Documentation:

```text
http://localhost:8000/docs
```

---

## Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## Environment Variables

### Backend (.env)

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/inventory_db
SECRET_KEY=mysecretkey123
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000
```

---

## Docker Setup

Build and start all services:

```bash
docker-compose up --build
```

Run in detached mode:

```bash
docker-compose up -d
```

Stop containers:

```bash
docker-compose down
```

---

## API Endpoints

### Products

| Method | Endpoint       |
| ------ | -------------- |
| GET    | /products      |
| GET    | /products/{id} |
| POST   | /products      |
| PUT    | /products/{id} |
| DELETE | /products/{id} |

### Customers

| Method | Endpoint        |
| ------ | --------------- |
| GET    | /customers      |
| GET    | /customers/{id} |
| POST   | /customers      |
| PUT    | /customers/{id} |
| DELETE | /customers/{id} |

### Orders

| Method | Endpoint     |
| ------ | ------------ |
| GET    | /orders      |
| GET    | /orders/{id} |
| POST   | /orders      |
| PUT    | /orders/{id} |
| DELETE | /orders/{id} |

---

## Deployment

### Backend Deployment (Render)

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

### Frontend Deployment (Vercel)

Framework:

```text
Vite
```

Build Command:

```bash
npm run build
```

Output Directory:

```text
dist
```

---

## Author

Ananya Bagre

B.Tech Mining Engineering, IIT (BHU) Varanasi

---

## License

This project is developed for educational and assessment purposes.
