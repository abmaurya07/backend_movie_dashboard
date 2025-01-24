from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.movies.models.movie import Movie
from decimal import Decimal

class MovieAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie1 = Movie.objects.create(
            title='Test Movie 1',
            year=2020,
            genre='Action',
            rating=8.5,
            one_line='Test description',
            stars='Actor 1, Actor 2',
            votes=1000,
            runtime=120,
            gross=Decimal('1000000.00')
        )
        self.movie2 = Movie.objects.create(
            title='Test Movie 2',
            year=2021,
            genre='Drama',
            rating=9.0,
            one_line='Another test description',
            stars='Actor 3, Actor 4',
            votes=2000,
            runtime=130,
            gross=Decimal('2000000.00')
        )

    def test_top_movies_by_gross(self):
        url = reverse('movies:top-by-gross')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Movie 2')

    def test_top_movies_by_votes(self):
        url = reverse('movies:top-by-votes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Movie 2')

    def test_top_movies_by_rating(self):
        url = reverse('movies:top-by-rating')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Movie 2')

    def test_movie_year_stats(self):
        url = reverse('movies:year-stats')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['total_movies'], 1) 