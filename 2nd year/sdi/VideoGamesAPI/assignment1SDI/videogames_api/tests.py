# Create your tests here.

from django.urls import resolve, reverse
from rest_framework.test import APITestCase

from videogames_api.views import *


class APIUrlsTests(APITestCase):
    statistic_url_games = reverse('by-avg-year')
    statistic_url_players = reverse('by-avg-age')

    def test_statistics_url_games(self):
        url = reverse("by-avg-year")
        self.assertEqual(resolve(url).route, "videogames/by-avg-year")

    def test_statistics_url_players(self):
        url = reverse("by-avg-age")
        self.assertEqual(resolve(url).route, "players/by-avg-age")

    def test_get_statistic1(self):
        response = self.client.get(self.statistic_url_games)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_statistic2(self):
        response2 = self.client.get(self.statistic_url_players)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
