"""
Movie API Views Test Module - Contains test cases for movie-related API endpoints.
This module tests the functionality of all movie API endpoints including data retrieval,
filtering, and statistical analysis features.
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.movies.models.movie import Movie
from decimal import Decimal


class MovieAPITestCase(TestCase):
    """
    Test case class for Movie API endpoints.
    Tests all API endpoints related to movie data retrieval and analysis.
    Includes tests for sorting by gross earnings, votes, ratings, and yearly statistics.
    """

    def setUp(self):
        """
        Set up test data before each test method.
        Creates two test movie instances with different attributes to test sorting and filtering.
        """
        self.client = APIClient()
        
        # Create first test movie with lower metrics
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
        
        # Create second test movie with higher metrics for comparison
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
        """
        Test the endpoint for retrieving movies sorted by gross earnings.
        Verifies that:
        1. The endpoint returns a successful response
        2. All movies are included in the response
        3. Movies are correctly sorted by gross earnings (highest first)
        """
        url = reverse('movies:top-by-gross')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Movie 2')  # Higher gross should be first

    def test_top_movies_by_votes(self):
        """
        Test the endpoint for retrieving movies sorted by number of votes.
        Verifies that:
        1. The endpoint returns a successful response
        2. All movies are included in the response
        3. Movies are correctly sorted by vote count (highest first)
        """
        url = reverse('movies:top-by-votes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Movie 2')  # Higher votes should be first

    def test_top_movies_by_rating(self):
        """
        Test the endpoint for retrieving movies sorted by rating.
        Verifies that:
        1. The endpoint returns a successful response
        2. All movies are included in the response
        3. Movies are correctly sorted by rating (highest first)
        """
        url = reverse('movies:top-by-rating')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Movie 2')  # Higher rating should be first

    def test_movie_year_stats(self):
        """
        Test the endpoint for retrieving movie statistics grouped by year.
        Verifies that:
        1. The endpoint returns a successful response
        2. Statistics are provided for each year
        3. The movie count per year is correct
        """
        url = reverse('movies:year-stats')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should have stats for 2 years
        self.assertEqual(response.data[0]['total_movies'], 1)  # Each year should have 1 movie 