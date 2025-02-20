#!/bin/bash

# Start the Docker containers
docker-compose up -d

# Wait for a few seconds to ensure the services are up and running
sleep 5

# Open Mongo-Express in the default web browser
open http://localhost:8081/