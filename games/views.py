from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Game, Player


def index(request):
    latest_game_list = Game.objects.order_by('-game_date')[:5]
    context = {'latest_game_list': latest_game_list}
    return render(request, 'games/index.html', context)


def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'games/detail.html', {'game': game})


def results(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'games/results.html', {'game': game})


def score(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    try:
        selected_player = game.player_set.get(pk=request.POST['player'])
    except (KeyError, Player.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'games/detail.html', {
            'game': game,
            'error_message': "You didn't select a player.",
        })
    else:
        selected_player.points += int(request.POST['score'])
        selected_player.difference_from_max = selected_player.game.max_score - \
            selected_player.points
        selected_player.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('games:detail', args=(game.id,)))
