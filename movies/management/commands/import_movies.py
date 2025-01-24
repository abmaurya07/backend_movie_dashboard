import pandas as pd
from decimal import Decimal
from django.core.management.base import BaseCommand
from movies.models import Movie
import decimal

def clean_gross(value):
    if pd.isna(value) or value == '' or value == 'NA':
        return None
    try:
        # First convert to float to handle scientific notation
        float_val = float(str(value).replace('$', '').replace(',', ''))
        # Then convert to string and Decimal to maintain precision
        return Decimal(str(float_val))
    except (ValueError, TypeError, decimal.ConversionSyntax):
        return None

def clean_votes(value):
    if pd.isna(value) or value == '' or value == 'NA':
        return 0
    try:
        # Remove any non-numeric characters except digits
        cleaned = ''.join(c for c in str(value) if c.isdigit())
        return int(cleaned) if cleaned else 0
    except (ValueError, TypeError):
        return 0

def clean_runtime(value):
    if pd.isna(value) or value == '' or value == 'NA':
        return 0
    try:
        return int(float(str(value)))
    except (ValueError, TypeError):
        return 0

def clean_year(value):
    if pd.isna(value) or value == '' or value == 'NA':
        return None
    try:
        year = int(float(str(value)))
        # Basic validation for reasonable year range
        return year if 1900 <= year <= 2025 else None
    except (ValueError, TypeError):
        return None

def clean_rating(value):
    if pd.isna(value) or value == '' or value == 'NA':
        return 0.0
    try:
        rating = float(str(value))
        # Basic validation for IMDb rating range (0-10)
        return rating if 0 <= rating <= 10 else 0.0
    except (ValueError, TypeError):
        return 0.0

class Command(BaseCommand):
    help = 'Import movies from CSV file'

    def handle(self, *args, **options):
        try:
            # Read the CSV file
            df = pd.read_csv('movies.csv')
            
            # Clean and transform data
            movies_to_create = []
            skipped_count = 0
            
            for _, row in df.iterrows():
                try:
                    movie = Movie(
                        title=str(row['MOVIES']) if not pd.isna(row['MOVIES']) else 'Unknown',
                        year=clean_year(row['YEAR']),
                        genre=str(row['GENRE']) if not pd.isna(row['GENRE']) else '',
                        rating=clean_rating(row['RATING']),
                        one_line=str(row['ONE-LINE']) if not pd.isna(row['ONE-LINE']) else '',
                        stars=str(row['STARS']) if not pd.isna(row['STARS']) else '',
                        votes=clean_votes(row['VOTES']),
                        runtime=clean_runtime(row['RunTime']),
                        gross=clean_gross(row['Gross'])
                    )
                    movies_to_create.append(movie)
                except Exception as row_error:
                    skipped_count += 1
                    self.stdout.write(
                        self.style.WARNING(f'Skipped row due to error: {str(row_error)}')
                    )
            
            # Bulk create movies
            if movies_to_create:
                Movie.objects.bulk_create(movies_to_create, batch_size=1000)
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully imported {len(movies_to_create)} movies'
                        + (f' (Skipped {skipped_count} rows)' if skipped_count > 0 else '')
                    )
                )
            else:
                self.stdout.write(
                    self.style.ERROR('No movies were imported')
                )
                
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR('Error: movies.csv file not found in the current directory')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error importing movies: {str(e)}')
            ) 