from django.db import models


class Game(models.Model):
    max_score = models.IntegerField(default=300)
    game_date = models.DateTimeField('date game started')


class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
