# Stage 1: Installation des dépendances
FROM python:slim-buster AS builder

WORKDIR /app

COPY requirements.txt .

# Installation des dépendances --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt


# Stage 2: Création de l'image finale
# Debugging step: List contents of potential package directory
RUN echo "--- Listing /usr/local/lib/python3.9/site-packages in builder stage ---"
RUN ls -l /usr/local/lib/python3.9/site-packages || true

# Stage 2: Création de l'image finale
FROM python:slim-buster AS stage-1
FROM python:slim-buster 

WORKDIR /app

# Copie des librairies installées (chemin corrigé)
COPY --from=builder /app /app

COPY . .

ENTRYPOINT ["python", "app.py"]