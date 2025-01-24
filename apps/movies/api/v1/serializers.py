from rest_framework import serializers
from apps.movies.models.movie import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'genre', 'rating', 'one_line', 'stars', 'votes', 'runtime', 'gross'] 