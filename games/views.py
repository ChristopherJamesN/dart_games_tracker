from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.http import HttpResponse

from .models import Game, Player


def index(request):
    latest_game_list = Game.objects.order_by('-game_date')[:5]
    context = {'latest_game_list': latest_game_list}
    return render(request, 'games/index.html', context)


def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'games/detail.html', {'game': game})


def results(request, game_id):
    response = "You're looking at the results of game %s."
    return HttpResponse(response % game_id)


def score(request, game_id):
    return HttpResponse("You're updating scores on game %s." % game_id)


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
        selected_player.votes += 1
        selected_player.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('game:results', args=(game.id,)))
