from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from teams.models import Team
from tournaments.models import Tournament
from sponsors.models import Sponsor
from .models import SignUpForm
from func.func import compare

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'forms/signup.html', {'form': form})

@login_required
def profile(request):
    
    user = get_object_or_404(User,pk=request.user.id)

    # seznam jeho requestu pokud je manager teamu
    requests_players = Team.objects.filter(managers=user)
    
    # seznam jeho requestu pokud je poradatel turnaje - na rozhodci a na hrace turnaje
    requests_tournaments = Tournament.objects.filter(poradatele=user)
    
    return render(request, 'forms/profile.html', {'user': user, 'requests_players':requests_players, 'requests_tournaments':requests_tournaments})

def request_player_remove(request, id, subid):
    team = get_object_or_404(Team, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        team.requests_users.remove(user)  
    return redirect('forms:profile')
    
def request_player_ok(request, id, subid):
    team = get_object_or_404(Team, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        team.players.add(user)
        team.requests_users.remove(user)  
    return redirect('forms:profile')


def request_rozhodci_remove(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        tournament.requests_rozhodci.remove(user) 
    return redirect('forms:profile')

def request_rozhodci_ok(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        tournament.rozhodci.add(user)
        team.requests_rozhodci.remove(user)
    return redirect('forms:profile')


def request_team_remove(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    team = get_object_or_404(Team, pk=subid)
    if request.method == 'POST':
        tournament.requests_teams.remove(team)
    return redirect('forms:profile')

def request_team_ok(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    team = get_object_or_404(Team, pk=subid)
    if request.method == 'POST':
        tournament.teams.add(team)
        tournament.requests_teams.remove(team) 
    return redirect('forms:profile')

# tlacitko chci hrat na profilu ciziho teamu
def request_add_player(request, id_t, id_u):
    team = get_object_or_404(Team, pk=id_t)
    user = get_object_or_404(User, pk=id_u)
    if request.method == 'POST':
        team.requests_players.add(user) 
    return redirect('forms:profile')

# tlacitko chci hrat na profilu ciziho teamu
def request_add_rozhodci(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        tournament.requests_rozhodci.add(user) 
    return redirect('forms:profile')

# tlacitko odstraneni usera z tymu
def remove_player(request, id, subid):
    team = get_object_or_404(Team, pk=id)
    user = get_object_or_404(User, pk=subid)
    if request.method == 'POST':
        team.players.remove(user) 
    if not len(team.players): # nezbyli tam zadny hraci, odstran tym
        team.delete()
    return redirect('forms:profile')

# tlacitko odstraneni sponzora z turnaje
def remove_sponsor(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    sponsor = get_object_or_404(Sponsor, pk=subid)
    if request.method == 'POST':
        tournament.sponsors.remove(sponsor) 
    return redirect('forms:profile')    

# tlacitko odstraneni rozhodciho z turnaje
def remove_rozhodci(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    rozhodci = get_object_or_404(User, pk=subid)
    if request.method == 'POST' and not tournament.started: # pri nastartovanem turnaji nejde odstranit rozhodci
        tournament.rozhodci.remove(rozhodci)
    return redirect('forms:profile')     

# tlacitko odstraneni teamu z turnaje
def remove_team(request, id, subid):
    tournament = get_object_or_404(Tournament, pk=id)
    team = get_object_or_404(Team, pk=subid)
    if request.method == 'POST' and not tournament.started: # pri nastartovanem turnaji nejde odstranit team
        tournament.teams.remove(team)
    return redirect('forms:profile')

# tlacitko odstraneni turnaje z povrchu tohoto nekvalitniho kodu
def delete_tournament(request, id):
    tournament = get_object_or_404(Tournament, pk=id)
    if request.method == 'POST' and not tournament.started: # pri nastartovanem turnaji nejde odstranit team
        tournament.delete()
    return redirect('forms:profile')

# tlacitko odstraneni tymu z povrchu tohoto nekvalitniho kodu
def delete_team(request, id):
    team = get_object_or_404(Team, pk=id)
    
    # vybere turnaje tohohle tymu
    my_tournaments = team.tour_teams.all()
    
    # vyber nastartovane turnaje a zjisti jestli v nejakem hraje tenhle tym
    started_tournaments = Tournament.objects.filter(started=True)
    
    if request.method == 'POST' and not compare(started_tournaments, my_tournaments): # zjisti jestli team nefiguruje v rozjetejch turnajich
        team.delete()
    return redirect('forms:profile')

# tlacitko chci pridat tym do turnaje
def request_add_team(request, id_tournament, id_team):
    team = get_object_or_404(Team, pk=id_team)
    tournament = get_object_or_404(Tournament, pk=id_tournament)
    if request.method == 'POST':
        tournament.requests_teams.add(team) 
    return redirect('forms:profile')


# BETA
#create new team

def create_team(request, id_u):
    user = get_object_or_404(User, pk=id_u)
    if request.method == 'POST':
        team.requests_players.add(user) 
    return redirect('forms:profile')
