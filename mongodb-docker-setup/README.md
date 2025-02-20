# MongoDB and Mongo Express Docker Setup

This project provides a simple setup for running MongoDB and Mongo Express using Docker. Follow the instructions below to get started.

## Prerequisites

- Docker installed on your machine
- Docker Compose installed

## Project Structure

```
mongodb-docker-setup
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## Getting Started

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd mongodb-docker-setup
   ```

2. **Build the Docker images** (if you are using a custom Dockerfile):
   ```bash
   docker-compose build
   ```

3. **Start the services**:
   ```bash
   docker-compose up
   ```

4. **Access Mongo Express**:
   Open your web browser and navigate to `http://localhost:8081` to access the Mongo Express interface.

5. **Access MongoDB**:
   MongoDB will be running on `mongodb://localhost:27017`.

## Stopping the Services

To stop the running services, press `CTRL+C` in the terminal where the services are running or run:
```bash
docker-compose down
```

## Configuration

You can customize the configuration in the `docker-compose.yml` file. This includes changing environment variables, ports, and other settings as needed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.