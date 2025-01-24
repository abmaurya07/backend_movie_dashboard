from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from .models import Movie

# Create your views here.

class TopMoviesByGrossView(APIView):
    def get(self, request):
        year = request.query_params.get('year')
        try:
            if year:
                year = int(year)
                movies = Movie.objects.filter(year=year, gross__isnull=False) \
                    .order_by('-gross')[:5]
            else:
                movies = Movie.objects.filter(gross__isnull=False) \
                    .order_by('-gross')[:5]
            
            data = [{
                'title': movie.title,
                'year': movie.year,
                'gross': float(movie.gross),
                'rating': movie.rating
            } for movie in movies]
            
            return Response(data)
        except ValueError:
            return Response(
                {'error': 'Invalid year parameter'},
                status=status.HTTP_400_BAD_REQUEST
            )

class TopMoviesByVotesView(APIView):
    def get(self, request):
        movies = Movie.objects.order_by('-votes')[:5]
        data = [{
            'title': movie.title,
            'year': movie.year,
            'votes': movie.votes,
            'rating': movie.rating
        } for movie in movies]
        
        return Response(data)

class TopMoviesByRatingView(APIView):
    def get(self, request):
        year = request.query_params.get('year')
        min_votes = request.query_params.get('min_votes', 1000)  # Default minimum votes
        
        try:
            if year:
                year = int(year)
                movies = Movie.objects.filter(year=year, votes__gte=min_votes) \
                    .order_by('-rating')[:10]
            else:
                movies = Movie.objects.filter(votes__gte=min_votes) \
                    .order_by('-rating')[:10]
            
            data = [{
                'title': movie.title,
                'year': movie.year,
                'rating': movie.rating,
                'votes': movie.votes
            } for movie in movies]
            
            return Response(data)
        except ValueError:
            return Response(
                {'error': 'Invalid year parameter'},
                status=status.HTTP_400_BAD_REQUEST
            )
