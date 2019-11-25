import random

from django.shortcuts import get_object_or_404, render, redirect
from .models import Tournament
from teams.models import Team
from sponsors.models import Sponsor
from matches.models import Match
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from forms.forms import AddTeamForm
from forms.forms import AddSponsorForm

from django.contrib import messages


def single(request, id):
    tournament = get_object_or_404(Tournament, pk=id)

    teams = tournament.teams.all()
    rozhodci = tournament.rozhodci.all()
    sponsors = tournament.sponsors.all()

    available_sponsors = Sponsor.objects.all()
    available_sponsors = available_sponsors.exclude(tour_sponsors__in=[tournament])

    add_new_team = None  # formular na pridani tymu do turnaje
    add_new_sponsor = None  # formular na pridani tymu do turnaje

    # vyber vsechny tymy ktere user managuje
    managing_teams = Team.objects.filter(managers=request.user)
    user = request.user
    available_teams = None
    permitted_add_team = False
    permitted_add_sponsor = False
    if not tournament.started:
        available_teams = managing_teams.exclude(tour_teams__in=[tournament])
        available_teams = available_teams.exclude(tour_requests_teams__in=[tournament])
        available_teams = available_teams.filter(singleplayerteam=tournament.singleplayer)

    tournament_referees = tournament.rozhodci.all()
    all_teams = Team.objects.all()
    if tournament_referees:
        for ref in tournament_referees:
            if available_teams:
                for t in available_teams:
                    for p in t.players.all():
                        if ref == p:
                            available_teams = available_teams.exclude(id=t.id)

    # ZACINA VALIDACE FORMULARE NA PRIDANI TYMU DO TURNAJE
    if request.method == 'POST':
        add_new_team = AddTeamForm(request.POST, t=available_teams)
        if add_new_team.is_valid():
            team = add_new_team.cleaned_data['teams']
            if team.managers == user and tournament.poradatele == user:
                tournament.teams.add(team)
            else:
                tournament.requests_teams.add(team)

            return single(request, id)

    # ZACINA VALIDACE FORMULARE NA PRIDANI SPONSORA DO TURNAJE
    if request.method == 'POST':
        add_new_sponsor = AddSponsorForm(request.POST, s=available_sponsors)
        if add_new_sponsor.is_valid():
            sponsors = add_new_sponsor.cleaned_data['sponsors']
            tournament.sponsors.add(sponsors)

            return single(request, id)

    if available_teams:
        if len(available_teams):
            add_new_team = AddTeamForm(t=available_teams)  # vytvor formular na pridani tymu do turnaje, az tedka
            permitted_add_team = True

    if available_sponsors:
        if len(available_sponsors):
            add_new_sponsor = AddSponsorForm(
                s=available_sponsors)  # vytvor formular na pridani tymu do turnaje, az tedka
            if user == tournament.poradatele:
                permitted_add_sponsor = True
            else:
                permitted_add_sponsor = False

    # vyber vsechny tymy, ve kterych je aktualni user
    his_teams = Team.objects.filter(players__in=[request.user])

    # zjisti jestli muze byt rozhodcim
    permitted = True
    s1 = set(his_teams)
    s2 = set(teams)
    if (s1 & s2):
        permitted = False

    tournament_started = tournament.started

    return render(request, 'tournaments/single.html', {'tournament': tournament, 'teams': teams, 'sponsors': sponsors,
                                                       'rozhodci': rozhodci, 'permitted': permitted,
                                                       'permitted_add_team': permitted_add_team,
                                                       'permitted_add_sponsor': permitted_add_sponsor,
                                                       'add_new_team': add_new_team,
                                                       'add_new_sponsor': add_new_sponsor,
                                                       'tournament_started': tournament_started})


def index(request):
    front = Tournament.objects.all()
    paginator = Paginator(front, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'tournaments/index.html', {'front': content})


@login_required
def your_tournaments(request):
    user = get_object_or_404(User, pk=request.user.id)
    tournaments = Tournament.objects.all()
    users_tournaments = []
    # select all teams where user is as a player
    for tour in tournaments:
        teams = tour.teams.all()
        for t in teams:
            players = t.players.all()
            for p in players:
                if p == user:
                    users_tournaments.append(tour)

    # select all teams where user is manager
    manage_tournaments = Tournament.objects.filter(poradatele=user)

    # merge arrays
    for t in manage_tournaments:
        users_tournaments.append(t)

    # unique array
    front_set = set(users_tournaments)
    front = list(front_set)

    paginator = Paginator(front, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    # front = Team.objects.filter(Q(managers=user), Q(players__in=[user]))  # vem tymy kde to ridi nebo v nich hraje
    return render(request, 'tournaments/index.html', {'front': content})


def start_tournament(request, id):
    tournament = get_object_or_404(Tournament, pk=id)
    teams = tournament.teams.all()
    player_count = teams.count()

    index = 0

    if teams.count() < 2:
        messages.warning(request, 'Wrong team count: ' + str(teams.count()) + '.')
        return single(request, id)
    else:
        while player_count > 1:
            if player_count % 2 != 0:
                messages.warning(request, 'Wrong number of teams. Must be power of two. ')
                return single(request, id)
            index += 1
            player_count /= 2

    for t in teams:
        players = t.players.all()
        if players.count() != tournament.player_count:
            messages.warning(request,
                             'Wrong player count in team ' + t.name + ' - ' + str(players.count()) + ' players.')
            return single(request, id)

    if len(tournament.rozhodci.all()) < 1:
        messages.warning(request,
                         'Tournament is missing a referee.')
        return single(request, id)

    if not tournament.started:
        new_matches(None, index, tournament)

    matches = Match.objects.filter(turnaj=tournament)
    teams = tournament.teams.all()

    if not tournament.started:
        fill_matches(matches, teams)
        tournament.started = True
        tournament.save()

    number_of_layers = index
    layers = []
    for i in range(1, number_of_layers + 1):
        layers.append(i)

    #     set winner when one of teams has higher score - means match finished
    winner = None
    for m in matches:
        if m.start_position == index:
            if m.score_A > m.score_B:
                winner = m.team_A
            elif m.score_B > m.score_A:
                winner = m.team_B

    is_referee = False
    referees = tournament.rozhodci.all()
    for r in referees:
        if r == request.user:
            is_referee = True

    return render(request, 'tournaments/match_schedule.html',
                  {'tournament': tournament, 'matches': matches, 'layers': layers, 'is_referee': is_referee})


# recurse function
# creates 2^index "spider" :D of matches which are connected
def new_matches(match, index, tournament):
    new_match = Match()
    if match:
        new_match.next_match = match
    new_match.start_position = index
    new_match.turnaj = tournament
    index -= 1
    new_match.save()
    if index > 0:
        new_matches(new_match, index, tournament)
        new_matches(new_match, index, tournament)


def fill_matches(matches, teams):
    first_matches = []
    first_matches_count = 0
    for m in matches:
        if m.start_position == 1:
            first_matches.append(m)
            first_matches_count += 1

    draw = []
    draw = random.sample(range(0, first_matches_count * 2), first_matches_count * 2)
    print(draw)
    print(len(teams))
    print(len(first_matches))

    i = 0
    for d in draw:
        a_b = i % 2
        pos = i // 2
        i += 1
        if a_b:
            first_matches[pos].team_A = teams[d]
            first_matches[pos].save()
        else:
            first_matches[pos].team_B = teams[d]
            first_matches[pos].save()
