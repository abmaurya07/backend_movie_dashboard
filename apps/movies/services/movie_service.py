"""
Movie Service Module - Handles all business logic related to movie data operations.
This module provides a service layer that abstracts database operations and complex queries
for the movie-related functionality.
"""

from django.db.models import F, Count, Avg
from apps.movies.models.movie import Movie


class MovieService:
    """
    Service class that handles all movie-related business logic and database operations.
    This class uses the Repository pattern to abstract database queries and provide
    clean interfaces for movie data manipulation.
    """

    @staticmethod
    def get_top_movies_by_gross(year=None, limit=5):
        """
        Retrieve top movies sorted by gross earnings.
        
        Args:
            year (int, optional): Filter movies by specific year. Defaults to None.
            limit (int, optional): Number of movies to return. Defaults to 5.
            
        Returns:
            QuerySet: List of movies ordered by gross earnings (highest to lowest).
        """
        queryset = Movie.objects.filter(gross__isnull=False)
        if year:
            queryset = queryset.filter(year=year)
        return queryset.order_by('-gross')[:limit]

    @staticmethod
    def get_top_movies_by_votes(limit=5):
        """
        Retrieve top movies sorted by number of votes.
        
        Args:
            limit (int, optional): Number of movies to return. Defaults to 5.
            
        Returns:
            QuerySet: List of movies ordered by vote count (highest to lowest).
        """
        return Movie.objects.order_by('-votes')[:limit]

    @staticmethod
    def get_top_movies_by_rating(year=None, min_votes=1000, limit=10):
        """
        Retrieve top-rated movies with a minimum vote threshold.
        
        Args:
            year (int, optional): Filter movies by specific year. Defaults to None.
            min_votes (int, optional): Minimum number of votes required. Defaults to 1000.
            limit (int, optional): Number of movies to return. Defaults to 10.
            
        Returns:
            QuerySet: List of movies ordered by rating (highest to lowest).
        """
        queryset = Movie.objects.filter(votes__gte=min_votes)
        if year:
            queryset = queryset.filter(year=year)
        return queryset.order_by('-rating')[:limit]

    @staticmethod
    def get_year_stats(start_year=None, end_year=None, min_movies=1):
        """
        Calculate movie statistics grouped by year.
        
        Args:
            start_year (int, optional): Start year for statistics calculation. Defaults to None.
            end_year (int, optional): End year for statistics calculation. Defaults to None.
            min_movies (int, optional): Minimum number of movies required per year. Defaults to 1.
            
        Returns:
            QuerySet: Yearly statistics including total movies and average rating.
        """
        queryset = Movie.objects.values('year')
        
        # Apply year range filters if specified
        if start_year:
            queryset = queryset.filter(year__gte=start_year)
        if end_year:
            queryset = queryset.filter(year__lte=end_year)

        return queryset.annotate(
            total_movies=Count('id'),
            average_rating=Avg('rating'),
            average_gross=Avg('gross')
        ).filter(total_movies__gte=min_movies).order_by('year') 