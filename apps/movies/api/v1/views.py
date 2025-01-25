"""
Movie API Views Module - Provides REST API endpoints for movie-related operations.
This module contains view classes that handle HTTP requests and responses for the movie API.
Each view is responsible for a specific aspect of movie data retrieval and processing.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.movies.services.movie_service import MovieService
from apps.movies.api.v1.serializers import MovieSerializer

class TopMoviesByGrossView(APIView):
    """
    API endpoint that retrieves top movies by gross earnings.
    
    GET /api/v1/movies/top-by-gross/
    
    Query Parameters:
        year (int, optional): Filter results by specific year
        
    Returns:
        200: List of movies ordered by gross earnings
        400: Bad request if year parameter is invalid
    """
    
    def get(self, request):
        """Handle GET request for top movies by gross earnings."""
        year = request.query_params.get('year')
        try:
            if year:
                year = int(year)
            movies = MovieService.get_top_movies_by_gross(year=year)
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response(
                {'error': 'Invalid year parameter'},
                status=status.HTTP_400_BAD_REQUEST
            )

class TopMoviesByVotesView(APIView):
    """
    API endpoint that retrieves top movies by number of votes.
    
    GET /api/v1/movies/top-by-votes/
    
    Returns:
        200: List of movies ordered by vote count
    """
    
    def get(self, request):
        """Handle GET request for top movies by votes."""
        movies = MovieService.get_top_movies_by_votes()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class TopMoviesByRatingView(APIView):
    """
    API endpoint that retrieves top-rated movies with optional filters.
    
    GET /api/v1/movies/top-by-rating/
    
    Query Parameters:
        year (int, optional): Filter results by specific year
        min_votes (int, optional): Minimum number of votes required (default: 1000)
        
    Returns:
        200: List of movies ordered by rating
        400: Bad request if parameters are invalid
    """
    
    def get(self, request):
        """Handle GET request for top movies by rating."""
        year = request.query_params.get('year')
        min_votes = request.query_params.get('min_votes', 1000)
        
        try:
            if year:
                year = int(year)
            min_votes = int(min_votes)
            movies = MovieService.get_top_movies_by_rating(
                year=year,
                min_votes=min_votes
            )
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response(
                {'error': 'Invalid parameter value'},
                status=status.HTTP_400_BAD_REQUEST
            )

class MovieYearStatsView(APIView):
    """
    API endpoint that provides statistical analysis of movies by year.
    
    GET /api/v1/movies/year-stats/
    
    Query Parameters:
        start_year (int, optional): Start year for analysis
        end_year (int, optional): End year for analysis
        min_movies (int, optional): Minimum number of movies per year (default: 1)
        
    Returns:
        200: List of yearly statistics including total movies and average rating
        400: Bad request if parameters are invalid
    """
    
    def get(self, request):
        """Handle GET request for movie statistics by year."""
        start_year = request.query_params.get('start_year')
        end_year = request.query_params.get('end_year')
        min_movies = request.query_params.get('min_movies', 1)

        try:
            # Convert string parameters to integers
            if start_year:
                start_year = int(start_year)
            if end_year:
                end_year = int(end_year)
            min_movies = int(min_movies)

            stats = MovieService.get_year_stats(
                start_year=start_year,
                end_year=end_year,
                min_movies=min_movies
            )
            
            # Format the response data
            data = [{
                'year': stat['year'],
                'total_movies': stat['total_movies'],
                'average_rating': round(stat['average_rating'], 2) if stat['average_rating'] else None,
                'average_gross': round(stat['average_gross'], 2) if stat['average_gross'] else None
            } for stat in stats]
            
            return Response(data)
        except ValueError:
            return Response(
                {'error': 'Invalid parameter value'},
                status=status.HTTP_400_BAD_REQUEST
            ) 