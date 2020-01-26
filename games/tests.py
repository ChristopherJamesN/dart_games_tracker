import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Game


class GameModelTests(TestCase):

    def test_was_started_recently_with_future_games(self):
        """
        was_played_recently() returns False for questions whose game_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_game = Game(game_date=time)
        self.assertIs(future_game.was_played_recently(), False)

    def test_was_played_recently_with_old_game(self):
        """
        was_played_recently() returns False for games whose game_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_game = Game(game_date=time)
        self.assertIs(old_game.was_played_recently(), False)

    def test_was_played_recently_with_recent_game(self):
        """
        was_played_recently() returns True for games whose game_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_game = Game(game_date=time)
        self.assertIs(recent_game.was_played_recently(), True)


def create_game(score, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Game.objects.create(max_score=score, game_date=time)


class GameIndexViewTests(TestCase):
    def test_no_gamess(self):
        """
        If no games exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('games:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No games are available.")
        self.assertQuerysetEqual(response.context['latest_game_list'], [])

    def test_past_game(self):
        """
        games with a game_date in the past are displayed on the
        index page.
        """
        create_game(score=400, days=-30)
        response = self.client.get(reverse('games:index'))
        self.assertQuerysetEqual(
            response.context['latest_game_list'],
            ['<Game: 400>']
        )
