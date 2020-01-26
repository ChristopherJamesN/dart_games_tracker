from django.shortcuts import render

from django.http import HttpResponse

from .models import Game


def index(request):
    latest_game_list = Game.objects.order_by('-game_date')[:5]
    context = {'latest_game_list': latest_game_list}
    return render(request, 'games/index.html', context)


def detail(request, game_id):
    return HttpResponse("You're looking at game %s." % game_id)


def results(request, game_id):
    response = "You're looking at the results of game %s."
    return HttpResponse(response % game_id)


def score(request, game_id):
    return HttpResponse("You're updating scores on game %s." % game_id)
