# backend/Dockerfile
FROM python:alpine3.21 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:alpine3.21
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
CMD ["python", "backend/app.py"]
