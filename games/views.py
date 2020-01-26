from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the games index.")


def detail(request, game_id):
    return HttpResponse("You're looking at game %s." % game_id)


def results(request, game_id):
    response = "You're looking at the results of game %s."
    return HttpResponse(response % game_id)


def score(request, game_id):
    return HttpResponse("You're updating scores on game %s." % game_id)
