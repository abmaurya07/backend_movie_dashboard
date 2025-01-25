# How To Guide

This document provides detailed instructions for common tasks and troubleshooting in the Movie Dashboard Backend project.

## Table of Contents
- [Development Setup](#development-setup)
- [Database Operations](#database-operations)
- [Working with Docker](#working-with-docker)
- [Data Import and Export](#data-import-and-export)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

## Development Setup

### First Time Setup with Docker

1. Clone and setup the project:
```bash
git clone <repository-url>
cd backend_movie_dashboard
cp .env.example .env
```

2. Start the Docker containers:
```bash
cd docker
docker-compose up --build
```

3. Run initial migrations:
```bash
docker-compose exec web python /app/server.py migrate
```

4. Import sample data (optional):
```bash
docker-compose exec web python /app/scripts/import_movies.py
```

### Local Development Setup

1. Set up Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env and set POSTGRES_HOST=localhost
```

3. Start PostgreSQL and create database:
```bash
# On Windows:
pg_ctl -D "C:\Program Files\PostgreSQL\13\data" start
createdb movie_dashboard

# On Linux/Mac:
sudo service postgresql start
createdb movie_dashboard
```

4. Run migrations and start server:
```bash
python server.py migrate
python server.py runserver
```

## Database Operations

### Working with Migrations

Create new migrations:
```bash
# With Docker:
docker-compose exec web python /app/server.py makemigrations

# Without Docker:
python server.py makemigrations
```

Apply migrations:
```bash
# With Docker:
docker-compose exec web python /app/server.py migrate

# Without Docker:
python server.py migrate
```

Show migration status:
```bash
# With Docker:
docker-compose exec web python /app/server.py showmigrations

# Without Docker:
python server.py showmigrations
```

### Database Backup and Restore

Backup:
```bash
# With Docker:
docker-compose exec db pg_dump -U postgres movie_dashboard > backup.sql

# Without Docker:
pg_dump -U postgres movie_dashboard > backup.sql
```

Restore:
```bash
# With Docker:
docker-compose exec -T db psql -U postgres movie_dashboard < backup.sql

# Without Docker:
psql -U postgres movie_dashboard < backup.sql
```

## Working with Docker

### Common Docker Commands

Start services:
```bash
docker-compose up -d
```

Stop services:
```bash
docker-compose down
```

View logs:
```bash
# All services
docker-compose logs

# Specific service
docker-compose logs web
docker-compose logs db
```

Rebuild containers:
```bash
docker-compose up --build
```

Access container shell:
```bash
# Web container
docker-compose exec web bash

# Database container
docker-compose exec db bash
```

### Docker Troubleshooting

1. Port conflicts:
```bash
# Check if ports are in use
netstat -ano | findstr :8000
netstat -ano | findstr :5432

# Change ports in docker-compose.yml if needed
ports:
  - "8001:8000"  # Maps host port 8001 to container port 8000
```

2. Database connection issues:
```bash
# Verify database is running
docker-compose ps

# Check database logs
docker-compose logs db

# Test database connection
docker-compose exec db psql -U postgres -d movie_dashboard -c "SELECT 1;"
```

## Data Import and Export

### Importing Movie Data

From CSV file:
```bash
# With Docker:
docker-compose exec web python /app/scripts/import_movies.py /app/movies.csv

# Without Docker:
python scripts/import_movies.py movies.csv
```

### Custom Data Import

Example script for custom data import:
```python
from apps.movies.models import Movie
from apps.movies.utils.data_cleaning import clean_gross, clean_year

def import_custom_data(file_path):
    with open(file_path, 'r') as f:
        # Your import logic here
        pass

# Usage
import_custom_data('path/to/data.csv')
```

## Testing

### Running Tests

Run all tests:
```bash
# With Docker:
docker-compose exec web python /app/server.py test

# Without Docker:
python server.py test
```

Run specific test:
```bash
# With Docker:
docker-compose exec web python /app/server.py test apps.movies.tests.test_api

# Without Docker:
python server.py test apps.movies.tests.test_api
```

### Test Coverage

Generate coverage report:
```bash
# With Docker:
docker-compose exec web coverage run /app/server.py test
docker-compose exec web coverage report

# Without Docker:
coverage run server.py test
coverage report
```

## Troubleshooting

### Common Issues

1. Database connection errors:
   - Check if database container is running
   - Verify POSTGRES_HOST in .env (should be 'db' for Docker, 'localhost' for local)
   - Ensure database port is not in use

2. Import errors:
   - Check PYTHONPATH in Docker environment
   - Verify virtual environment is activated (for local development)
   - Check file permissions for CSV files

3. Migration issues:
   - Try resetting migrations: `python server.py migrate --fake-initial`
   - Check for conflicting migrations
   - Verify database connection

### Logging

Enable debug logging in .env:
```
DEBUG=True
```

View Django logs:
```bash
# With Docker:
docker-compose logs web

# Without Docker:
python server.py runserver --verbosity 2
```

### Performance Optimization

1. Database indexing:
```python
class Movie(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['year']),
            models.Index(fields=['rating']),
        ]
```

2. Bulk operations:
```python
# Efficient bulk create
Movie.objects.bulk_create(movie_objects)

# Efficient bulk update
Movie.objects.bulk_update(movie_objects, ['field1', 'field2'])
```

3. Query optimization:
```python
# Use select_related for foreign keys
Movie.objects.select_related('category').all()

# Use prefetch_related for many-to-many
Movie.objects.prefetch_related('actors').all()
``` 