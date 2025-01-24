import pandas as pd
import os
import django
from decimal import Decimal

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_dashboard.settings')
django.setup()

from movies.models import Movie

def clean_gross(value):
    if pd.isna(value):
        return None
    # Remove '$' and ',' from the string and convert to Decimal
    return Decimal(str(value).replace('$', '').replace(',', ''))

def import_movies():
    # Read the CSV file
    df = pd.read_csv('movies.csv')
    
    # Clean and transform data
    movies_to_create = []
    for _, row in df.iterrows():
        movie = Movie(
            title=row['MOVIES'],
            year=int(row['YEAR']),
            genre=row['GENRE'],
            rating=float(row['RATING']),
            one_line=row['ONE-LINE'],
            stars=row['STARS'],
            votes=int(row['VOTES']),
            runtime=int(row['RunTime']),
            gross=clean_gross(row['Gross'])
        )
        movies_to_create.append(movie)
    
    # Bulk create movies
    Movie.objects.bulk_create(movies_to_create, batch_size=1000)
    print(f"Successfully imported {len(movies_to_create)} movies")

if __name__ == '__main__':
    import_movies() 