# Stage 1: Installation des dépendances
FROM python:alpine3.21 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Création de l'image finale
FROM python:alpine3.21

WORKDIR /app

# Copie des dépendances installées depuis le builder
COPY --from=builder /app/ .

COPY . .

COPY entrypoint.sh /app/

RUN chmod +x /app/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]