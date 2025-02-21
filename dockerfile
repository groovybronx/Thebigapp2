# Stage 1: Build dependencies
FROM python:3.9-slim-buster AS builder 
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Create final image
FROM python:3.9-slim-buster  
WORKDIR /app
COPY --from=builder /app/requirements.txt .  
COPY . .  
COPY entrypoint.sh /app/ 
RUN chmod +x /app/entrypoint.sh # Make it executable

# Expose the port your Flask app listens on
EXPOSE 5000 

# Define the entrypoint to start your application
ENTRYPOINT ["/app/entrypoint.sh"]