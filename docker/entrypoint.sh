#!/bin/bash

# Wait for postgres
echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Run migrations
echo "Running migrations..."
python server.py migrate

# Start command
exec "$@" 