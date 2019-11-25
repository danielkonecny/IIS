from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from teams.models import Team
from tournaments.models import Tournament
from sponsors.models import Sponsor
from matches.models import Match
from .models import SignUpForm
from django.forms.models import model_to_dict
from tournaments.views import single, start_tournament

from .forms import AddTeamForm, TournamentForm, CreateTournament, CreateTeam, CreateSponsor, AddMatchResultsForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'New profile created.')
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'forms/signup.html', {'form': form})


@login_required
def profile(request):
    # seznam jeho requestu pokud je manager teamu
    requests_players = Team.objects.filter(managers=request.user)
    # seznam jeho requestu pokud je poradatel turnaje - na rozhodci a na hrace turnaje
    requests_tournaments = Tournament.objects.filter(poradatele=request.user)
    return render(request, 'forms/profile.html', {'user': request.user, 'requests_players': requests_players,
                                                  'requests_tournaments': requests_tournaments})


# odstran hrace z requestu
def request_player_remove(request, id, subid):
    team = get_object_or_404(Team, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        team.requests_users.remove(user)
        messages.success(request, 'Request removed.')
    return redirect('forms:profile')


# prijmi hrace do tymu    
def request_player_ok(request, id, subid):
    team = get_object_or_404(Team, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        team.players.add(user)
        team.requests_users.remove(user)
        messages.success(request, 'Request accepted.')
    return redirect('forms:profile')


# odstran request rozhodciho z turnaje
def request_rozhodci_remove(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        tournament.requests_rozhodci.remove(user)
        messages.success(request, 'Request removed.')
    return redirect('forms:profile')


# prijmi rozhodciho na turnaj
def request_rozhodci_ok(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        tournament.rozhodci.add(user)
        tournament.requests_rozhodci.remove(user)
        messages.success(request, 'Request accepted.')
    return redirect('forms:profile')


# odstran request teamu poradatelem turnaje
def request_team_remove(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    team = get_object_or_404(Team, pk=subid)
    if request.method == 'POST':
        tournament.requests_teams.remove(team)
        messages.success(request, 'Request removed.')
    return redirect('forms:profile')


# prijeti tymu na turnaj poradatelem
def request_team_ok(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    team = get_object_or_404(Team, pk=subid)
    if request.method == 'POST':
        tournament.teams.add(team)
        tournament.requests_teams.remove(team)
        messages.success(request, 'Request accepted.')
    return redirect('forms:profile')


# tlacitko chci hrat na profilu ciziho teamu
def request_add_player(request, id_t, id_u):
    team = get_object_or_404(Team, pk=id_t)
    user = get_object_or_404(User, pk=id_u)
    if team.managers.id == user.id:
        if request.method == 'POST':
            team.players.add(user)
            messages.success(request, 'Player added.')
    else:
        if request.method == 'POST':
            team.requests_users.add(user)
            messages.success(request, 'Request sent.')
    return redirect('teams:single', team.id)


# tlacitko chci rozhodcovat na profilu ciziho teamu
def request_add_rozhodci(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        if user == tournament.poradatele:
            tournament.rozhodci.add(user)
            messages.success(request, 'Referee added.')
        else:
            tournament.requests_rozhodci.add(user)
            messages.success(request, 'Request sent.')
    return redirect('tournaments:single', id)


# tlacitko odstraneni usera z tymu
def remove_player(request, id, subid):
    team = get_object_or_404(Team, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        team.players.remove(user)
        messages.success(request, 'Player removed.')
        #     nebudeme mazat tym bez hracu + if not team.players.count nefunguje
        # if not team.players.count: # nezbyli tam zadny hraci, odstran tym
        #     team.delete()
        #     messages.success(request, 'Last player removed and team deleted.')
        #     return redirect('forms:profile')
        # else:
    return redirect('teams:single', team.id)


# tlacitko odstraneni sponzora z turnaje
def remove_sponsor(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    sponsor = get_object_or_404(Sponsor, pk=subid)
    if request.method == 'POST':
        tournament.sponsors.remove(sponsor)
        messages.success(request, 'Sponsor removed.')
    return single(request, id)


# tlacitko odstraneni rozhodciho z turnaje
def remove_rozhodci(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    rozhodci = get_object_or_404(User, pk=subid)
    if request.method == 'POST' and not tournament.started:  # pri nastartovanem turnaji nejde odstranit rozhodci
        tournament.rozhodci.remove(rozhodci)
        messages.success(request, 'Rozhodci removed.')
    return single(request, id)


# tlacitko odstraneni teamu z turnaje
def remove_team(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    team = get_object_or_404(Team, pk=subid)
    if request.method == 'POST' and not tournament.started:  # pri nastartovanem turnaji nejde odstranit team
        tournament.teams.remove(team)
        messages.success(request, 'Team removed.')
    return single(request, id)


# tlacitko odstraneni turnaje z povrchu tohoto nekvalitniho kodu
def delete_tournament(request, id):
    tournament = get_object_or_404(Tournament, pk=id)
    if request.method == 'POST' and not tournament.started:  # pri nastartovanem turnaji nejde odstranit team
        tournament.delete()
        messages.success(request, 'Tournament deleted.')
    return redirect('tournaments:index')


# tlacitko odstraneni tymu z povrchu tohoto nekvalitniho kodu
def delete_team(request, id):
    team = get_object_or_404(Team, pk=id)

    # vybere turnaje tohohle tymu
    my_tournaments = team.tour_teams.all()

    # vyber nastartovane turnaje a zjisti jestli v nejakem hraje tenhle tym
    started_tournaments = Tournament.objects.filter(started=True)

    if request.method == 'POST' and not compare(started_tournaments,
                                                my_tournaments):  # zjisti jestli team nefiguruje v rozjetejch turnajich
        team.delete()
        messages.success(request, 'Team deleted.')
    return redirect('teams:index')


# uprav svuj turnaj
def edit_tournament(request, id):
    tournament = get_object_or_404(Tournament, pk=id)
    if request.method == 'POST':
        form = TournamentForm(request.POST, instance=tournament)
        if form.is_valid():
            new = form.save(commit=False)
            if new.singleplayer:
                new.player_count = 1
            new.save()
            messages.success(request, 'Tournament saved.')
            return redirect('tournaments:index')
    else:
        form = TournamentForm(instance=tournament)
    return render(request, 'forms/edit_tournament.html', {'edit': form, 'tournament': tournament})


# vytvor novej turnaj
def create_tournament(request):
    if request.method == 'POST':
        form = CreateTournament(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.poradatele = request.user
            if new.singleplayer == True:
                new.player_count = 1
            new.save()
            messages.success(request, 'Tournament created.')
            return redirect('tournaments:index')

    else:
        form = CreateTournament()
    return render(request, 'forms/add_tournament.html', {'edit': form})


# vytvor novej tym. Tym upravit nejde, potreba ho smazat a zalozit dalsi.
def create_team(request):
    if request.method == 'POST':
        form = CreateTeam(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.managers = request.user
            new.save()
            messages.success(request, 'Team created.')
            return redirect('teams:index')

    else:
        form = CreateTeam()
    return render(request, 'forms/add_team.html', {'edit': form})


# vytvor sponsora. Tym upravit nejde, potreba ho smazat a zalozit dalsi.
def create_sponsor(request):
    if request.method == 'POST':
        form = CreateSponsor(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            # new.managers = request.user
            new.save()
            messages.success(request, 'Sponsor created.')
            return redirect('sponsors:index')

    else:
        form = CreateSponsor()
    return render(request, 'forms/add_sponsor.html', {'edit': form})


# uprav vysledky zapasu
def add_match_results(request, id):
    match = get_object_or_404(Match, pk=id)
    tournament_id = match.turnaj.id
    if request.method == 'POST':
        form = AddMatchResultsForm(request.POST, instance=match)
        if form.is_valid():
            new = form.save(commit=False)

            next_match = match.next_match

            winner = None
            if match.score_A == match.score_B:
                messages.warning(request, 'Teams cannot have same score.')
                return start_tournament(request, tournament_id)

            new.save()
            if match.score_A > match.score_B:
                winner = match.team_A
            else:
                winner = match.team_B

            if next_match:
                if next_match.team_A is None:
                    next_match.team_A = winner
                else:
                    next_match.team_B = winner

                next_match.save()
            else:
                match.turnaj.winner = winner
                match.turnaj.save()

            messages.success(request, 'Match results saved.')
            return start_tournament(request, tournament_id)
    else:
        form = AddMatchResultsForm(instance=match)
    return render(request, 'forms/add_match_results.html', {'edit': form, 'match': match})
