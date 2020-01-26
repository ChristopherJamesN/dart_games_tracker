import datetime

from django.db import models
from django.utils import timezone


class Game(models.Model):
    max_score = models.IntegerField(default=300)
    game_date = models.DateTimeField('date game started')

    def __str__(self):
        return str(self.max_score)

    def was_played_recently(self):
        return self.game_date >= timezone.now() - datetime.timedelta(days=1)


class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
