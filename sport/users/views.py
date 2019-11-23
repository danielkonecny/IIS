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


def players(request):
    # players = get_user_model().objects.filter(team_teams=True)
    teams = Team.objects.all()
    players_arr = []
    for t in teams:
        team_players = t.players.all()
        for p in team_players:
            players_arr.append(p)

    unique = set(players_arr)
    front = list(unique)

    paginator = Paginator(front, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'users/players.html', {'players': content})


def managers(request):
    # players = get_user_model().objects.filter(team_managers=True)
    teams = Team.objects.all()
    managers_arr = []
    for t in teams:
        team_players = t.players.all()
        for p in team_players:
            managers_arr.append(p)

    unique = set(managers_arr)
    front = list(unique)

    paginator = Paginator(front, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'users/managers.html', {'players': content})


def referees(request):
    # players = get_user_model().objects.filter(tour_referees=True)

    tournaments = Tournament.objects.all()
    referees_arr = []
    for t in tournaments:
        tournament_referees = t.rozhodci.all()
        for r in tournament_referees:
            referees_arr.append(r)

    unique = set(referees_arr)
    front = list(unique)

    paginator = Paginator(front, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'users/referees.html', {'players': content})
