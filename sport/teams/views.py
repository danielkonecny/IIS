from django.shortcuts import get_object_or_404, render
from .models import Team
from tournaments.models import Tournament
from func.func import compare
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from matches.models import Match
from django.db.models import Q  # , Count
from django.core.paginator import Paginator


def single(request, id):
    team = get_object_or_404(Team, pk=id)

    tournaments = team.tour_teams.all()
    players = team.players.all()
    manager = team.managers

    # zjistit jestli zobrazovat delete team tlacitko
    active_tournaments = Tournament.objects.filter(started=True)
    permitted = not compare(tournaments, active_tournaments)

    # zjisti jestli se muze nabidnout do tymu jako hrac

    able_to_play = True
    if team.singleplayerteam and team.players.count():
        able_to_play = False

    matches = Match.objects.all()
    teams_matches = []
    won_matches = []
    for m in matches:
        if m.team_A == team:
            teams_matches.append(m)
            if m.score_A > m.score_B:
                won_matches.append(m)
        if m.team_B == team:
            teams_matches.append(m)
            if m.score_B > m.score_A:
                won_matches.append(m)

    if len(won_matches) == 0:
        percentage = 0
    else:
        percentage = len(won_matches) / len(teams_matches) * 100

    return render(request, 'teams/single.html',
                  {'team': team, 'tournaments': tournaments, 'players': players, 'manager': manager,
                   'permitted': permitted, 'able_to_play': able_to_play, 'teams_matches': teams_matches, 'won_matches': won_matches, 'percentage': percentage})


def index(request):
    front = Team.objects.all()
    paginator = Paginator(front, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'teams/index.html', {'front': content})


@login_required
def your_teams(request):
    user = get_object_or_404(User, pk=request.user.id)
    teams = Team.objects.all()
    users_teams = []
    # select all teams where user is as a player
    for t in teams:
        players = t.players.all()
        for p in players:
            if p == user:
                users_teams.append(t)
    # select all teams where user is manager
    manage_teams = Team.objects.filter(managers=user)
    for t in manage_teams:
        users_teams.append(t)

    # unique array
    front_set = set(users_teams)
    front = list(front_set)

    paginator = Paginator(front, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    # front = Team.objects.filter(Q(managers=user), Q(players__in=[user]))  # vem tymy kde to ridi nebo v nich hraje
    return render(request, 'teams/index.html', {'front': content})
