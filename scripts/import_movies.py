import os
import sys
import django
import pandas as pd

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from apps.movies.models.movie import Movie
from apps.movies.utils.data_cleaning import (
    clean_gross,
    clean_year,
    clean_rating,
    clean_votes,
    clean_runtime
)

def import_movies(csv_path='movies.csv'):
    """Import movies from CSV file."""
    try:
        # Read the CSV file
        df = pd.read_csv(csv_path, dtype={'Gross': str})
        
        # Clean and transform data
        movies_to_create = []
        skipped_count = 0
        
        for _, row in df.iterrows():
            try:
                # Clean the votes value and default to 0 if None
                votes_value = clean_votes(row['VOTES'])
                if votes_value is None:
                    votes_value = 0
                    
                # Clean the runtime value and default to 0 if None
                runtime_value = clean_runtime(row['RunTime'])
                if runtime_value is None:
                    runtime_value = 0
                    
                movie = Movie(
                    title=str(row['MOVIES']) if not pd.isna(row['MOVIES']) else 'Unknown',
                    year=clean_year(row['YEAR']),
                    genre=str(row['GENRE']) if not pd.isna(row['GENRE']) else '',
                    rating=clean_rating(row['RATING']),
                    one_line=str(row['ONE-LINE']) if not pd.isna(row['ONE-LINE']) else '',
                    stars=str(row['STARS']) if not pd.isna(row['STARS']) else '',
                    votes=votes_value,
                    runtime=runtime_value,
                    gross=clean_gross(row['Gross'])
                )
                movies_to_create.append(movie)
            except Exception as e:
                skipped_count += 1
                print(f'Skipped row due to error: {str(e)}')
        
        # First, delete existing movies to avoid duplicates
        Movie.objects.all().delete()
        
        # Bulk create movies
        if movies_to_create:
            Movie.objects.bulk_create(movies_to_create, batch_size=1000)
            print(f'Successfully imported {len(movies_to_create)} movies'
                  + (f' (Skipped {skipped_count} rows)' if skipped_count > 0 else ''))
        else:
            print('No movies were imported')
            
    except FileNotFoundError:
        print(f'Error: {csv_path} file not found in the current directory')
    except Exception as e:
        print(f'Error importing movies: {str(e)}')

if __name__ == '__main__':
    import_movies() 