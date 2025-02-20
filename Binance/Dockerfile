# Backend Dockerfile
FROM python:3.9-slim as backend

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ .

CMD ["python", "app.py"]

# Frontend Dockerfile
FROM node:14 as frontend

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ .

CMD ["npm", "start"]