import datetime

from django.test import TestCase
from django.utils import timezone

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
