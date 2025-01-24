from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.movies.services.movie_service import MovieService
from apps.movies.api.v1.serializers import MovieSerializer

class TopMoviesByGrossView(APIView):
    def get(self, request):
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
    def get(self, request):
        movies = MovieService.get_top_movies_by_votes()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class TopMoviesByRatingView(APIView):
    def get(self, request):
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
    def get(self, request):
        start_year = request.query_params.get('start_year')
        end_year = request.query_params.get('end_year')
        min_movies = request.query_params.get('min_movies', 1)

        try:
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
            
            data = [{
                'year': stat['year'],
                'total_movies': stat['total_movies'],
                'average_rating': round(stat['average_rating'], 2) if stat['average_rating'] else None
            } for stat in stats]
            
            return Response(data)
        except ValueError:
            return Response(
                {'error': 'Invalid parameter value'},
                status=status.HTTP_400_BAD_REQUEST
            ) 