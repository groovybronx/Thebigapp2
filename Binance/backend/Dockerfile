# Stage 1: Installation des dépendances
FROM python:alpine3.21 AS builder

WORKDIR /app

COPY requirements.txt .

# Installation des dépendances --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Création de l'image finale
FROM python:alpine3.21

WORKDIR /app

# Copie des librairies installées (chemin corrigé)
COPY --from=builder /root/.local/lib/python3.9/site-packages /app/lib/python3.9/site-packages

COPY . .

ENTRYPOINT ["python", "backend/app.py"]