from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from teams.models import Team
from tournaments.models import Tournament


def single(request, id):
    user = get_object_or_404(User, pk=id)
    teams = user.team_teams.all()

    return render(request, 'users/single.html', {'user': user, 'teams': teams})


# def players(request):
#     # players = get_user_model().objects.filter(team_teams=True)
#     teams = Team.objects.all()
#     players = []
#     for t in teams:
#         team_players = t.players.all()
#         for p in team_players:
#             players.append(p)
#
#     unique = set(players)
#     front = list(unique)
#
#     paginator = Paginator(front, 10)
#     page = request.GET.get('page')
#     content = paginator.get_page(page)
#     return render(request, 'users/players.html', {'players': content})
#

# def managers(request):
#     # players = get_user_model().objects.filter(team_managers=True)
#     # teams = Team.objects.all()
#     # managers = []
#     # for t in teams:
#     #     team_players = t.players.all()
#     #     for p in team_players:
#     #         managers.append(p)
#     #
#     # unique = set(managers)
#     # front = list(unique)
#
#     front = User.objects.all()
#
#
#     paginator = Paginator(front, 10)
#     page = request.GET.get('page')
#     content = paginator.get_page(page)
#     return render(request, 'users/managers.html', {'players': content})
#
#
# def rozhodci(request):
#     # players = get_user_model().objects.filter(tour_rozhodci=True)
#
#     tournaments = Tournament.objects.all()
#     referees = []
#     for t in tournaments:
#         tournament_referees = t.rozhodci.all()
#         for r in tournament_referees:
#             referees.append(r)
#
#     unique = set(referees)
#     front = list(unique)
#
#     paginator = Paginator(front, 10)
#     page = request.GET.get('page')
#     content = paginator.get_page(page)
#     return render(request, 'users/rozhodci.html', {'players': content})


def all(request):
    users = User.objects.all()

    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)

    return render(request, 'users/all.html', {'users': content})
