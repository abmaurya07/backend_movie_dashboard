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

- Python 3.x
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Docker support

## Prerequisites

- Python 3.x
- PostgreSQL 12+
- Docker (optional)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd backend_movie_dashboard
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Create PostgreSQL database:
```bash
createdb movie_dashboard
```

6. Run database migrations:
```bash
python manage.py migrate
```

## Running the Application

### Development Server
```bash
python manage.py runserver
```

### Docker
```bash
docker-compose up --build
```

### Utility Scripts

#### Import Movies Script
The project includes a utility script to import movie data from a CSV file into the database.

```bash
# Import movies from the default movies.csv file in the root directory
python scripts/import_movies.py

# Import movies from a custom CSV file
python scripts/import_movies.py path/to/your/movies.csv
```

The script performs the following operations:
- Reads movie data from a CSV file
- Cleans and validates data (gross earnings, year, rating, votes, runtime)
- Removes existing movies to avoid duplicates
- Bulk imports the cleaned movie data into the database

**Note**: Ensure your virtual environment is activated and all dependencies are installed before running the script.

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
python manage.py test
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
├── requirements/
└── scripts/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with Django REST Framework 