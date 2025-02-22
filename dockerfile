# Stage 1: Installation des dépendances
FROM python:slim-buster AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Debugging step: List contents of potential package directory
RUN echo "--- Listing /usr/local/lib/python3.9/site-packages in builder stage ---"
RUN ls -l /usr/local/lib/python3.9/site-packages || true

# Stage 2: Création de l'image finale
FROM python:slim-buster AS stage-1
FROM python:slim-buster 

WORKDIR /app

# Copie des dépendances installées depuis le builder
COPY --from=builder /app/ .

COPY . .

COPY entrypoint.sh /app/

RUN chmod +x /app/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]