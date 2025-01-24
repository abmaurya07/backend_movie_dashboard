from django.urls import path
from apps.movies.api.v1.views import (
    TopMoviesByGrossView,
    TopMoviesByVotesView,
    TopMoviesByRatingView,
    MovieYearStatsView
)

app_name = 'movies'

urlpatterns = [
    path('top-by-gross/', TopMoviesByGrossView.as_view(), name='top-by-gross'),
    path('top-by-votes/', TopMoviesByVotesView.as_view(), name='top-by-votes'),
    path('top-by-rating/', TopMoviesByRatingView.as_view(), name='top-by-rating'),
    path('year-stats/', MovieYearStatsView.as_view(), name='year-stats'),
] 