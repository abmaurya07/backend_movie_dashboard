from django.urls import path
from .views import TopMoviesByGrossView, TopMoviesByVotesView, TopMoviesByRatingView

urlpatterns = [
    path('top-by-gross/', TopMoviesByGrossView.as_view(), name='top-by-gross'),
    path('top-by-votes/', TopMoviesByVotesView.as_view(), name='top-by-votes'),
    path('top-by-rating/', TopMoviesByRatingView.as_view(), name='top-by-rating'),
] 