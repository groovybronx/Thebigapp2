# Stage 1: Installation des dépendances
FROM python:3.9-slim-buster AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Création de l'image finale
FROM python:3.9-slim-buster
WORKDIR /app
COPY --from=builder /app/requirements.txt .
COPY . .  
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]