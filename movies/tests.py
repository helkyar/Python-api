from django.test import TestCase

# Create your tests here.
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase
    
from django.urls import reverse
    
    
class GetGenresTest(APITestCase):
""" Test module for GET genres """
    def setUp(self):
        self.genres = []
        self.genres.append(baker.make('cars.Brand', name='a'))
        self.genres.append(baker.make('cars.Brand', name='b'))
        self.genres_counter = len(self.genres)
        self.url = reverse('genres')
        
    def test_get_genres_valid(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), self.genres_counter)
        self.assertEqual(response.data['results'][0]['id'], self.genres[0].id)
        self.assertEqual(response.data['results'][1]['id'], self.genres[1].id)
