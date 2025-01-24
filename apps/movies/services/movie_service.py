from django.db.models import F, Count, Avg
from apps.movies.models.movie import Movie

class MovieService:
    @staticmethod
    def get_top_movies_by_gross(year=None, limit=5):
        queryset = Movie.objects.filter(gross__isnull=False)
        if year:
            queryset = queryset.filter(year=year)
        return queryset.order_by('-gross')[:limit]

    @staticmethod
    def get_top_movies_by_votes(limit=5):
        return Movie.objects.order_by('-votes')[:limit]

    @staticmethod
    def get_top_movies_by_rating(year=None, min_votes=1000, limit=10):
        queryset = Movie.objects.filter(votes__gte=min_votes)
        if year:
            queryset = queryset.filter(year=year)
        return queryset.order_by('-rating')[:limit]

    @staticmethod
    def get_year_stats(start_year=None, end_year=None, min_movies=1):
        queryset = Movie.objects.values('year')
        
        if start_year:
            queryset = queryset.filter(year__gte=start_year)
        if end_year:
            queryset = queryset.filter(year__lte=end_year)

        return queryset.annotate(
            total_movies=Count('id'),
            average_rating=Avg('rating')
        ).filter(total_movies__gte=min_movies).order_by('year') 