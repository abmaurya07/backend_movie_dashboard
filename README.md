# Movie Dashboard Backend

A robust REST API backend for managing and analyzing movie data. Built with Django REST Framework, this service provides endpoints for retrieving movie information, statistics, and analytics.

## Features

- 🎬 Movie data management and retrieval
- 📊 Statistical analysis by year
- 🏆 Top movies by different metrics (gross earnings, votes, ratings)
- 🔒 Secure API endpoints
- 📝 Comprehensive data validation and cleaning
- 🧪 Extensive test coverage

## Tech Stack

- Python 3.11
- Django REST Framework
- PostgreSQL 13
- JWT Authentication
- Docker & Docker Compose

## Prerequisites

- Python 3.11+
- PostgreSQL 13+
- Docker and Docker Compose (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd backend_movie_dashboard
```

### Using Docker (Recommended)

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Build and start the containers:
```bash
cd docker
docker-compose up --build
```

The application will be available at `http://localhost:8000`

### Manual Setup (Alternative)

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
# Make sure POSTGRES_HOST=localhost for local development
```

4. Create PostgreSQL database:
```bash
createdb movie_dashboard
```

5. Run database migrations:
```bash
python server.py migrate
```

## Running the Application

### Using Docker
```bash
cd docker
docker-compose up
```

### Local Development Server
```bash
python server.py runserver
```

### Utility Scripts

#### Import Movies Script
The project includes a utility script to import movie data from a CSV file into the database.

```bash
# With Docker:
docker-compose exec web python scripts/import_movies.py

# Without Docker:
python scripts/import_movies.py path/to/your/movies.csv
```

The script performs the following operations:
- Reads movie data from a CSV file
- Cleans and validates data (gross earnings, year, rating, votes, runtime)
- Removes existing movies to avoid duplicates
- Bulk imports the cleaned movie data into the database

## API Endpoints

### REST API

#### Movies
- `GET /api/v1/movies/top-by-gross/`
  - Get top movies by gross earnings
  - Query params: `year` (optional)

- `GET /api/v1/movies/top-by-votes/`
  - Get top movies by number of votes

- `GET /api/v1/movies/top-by-rating/`
  - Get top rated movies
  - Query params: `year` (optional), `min_votes` (default: 1000)

- `GET /api/v1/movies/year-stats/`
  - Get movie statistics by year
  - Query params: `start_year`, `end_year`, `min_movies` (default: 1)

## Data Cleaning

The application includes robust data cleaning utilities for:
- Gross earnings (handles currency symbols, K/M suffixes)
- Year validation
- Rating normalization
- Vote count processing
- Runtime standardization

## Testing

Run the test suite:

```bash
# With Docker:
docker-compose exec web python server.py test

# Without Docker:
python server.py test
```

## Project Structure

```
backend_movie_dashboard/
├── apps/
│   └── movies/
│       ├── api/
│       ├── models/
│       ├── services/
│       ├── tests/
│       └── utils/
├── config/
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── requirements/
└── scripts/
```

## Environment Variables

Key environment variables in `.env`:
```
DEBUG=True
SECRET_KEY=your-secret-key
POSTGRES_DB=movie_dashboard
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=db  # Use 'db' for Docker, 'localhost' for local development
POSTGRES_PORT=5432
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with Django REST Framework 