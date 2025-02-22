FROM python:alpine3.21 AS builder

WORKDIR /app

COPY ../requirements.txt . 

# Installation des dépendances --user et --no-cache-dir
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:alpine3.21

WORKDIR /app

# Copie des librairies installées (chemin corrigé)
COPY --from=builder /root/.local /root/.local

COPY . .

ENTRYPOINT ["python", "backend/app.py"]
