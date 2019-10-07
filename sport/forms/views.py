from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from teams.models import Team
from tournaments.models import Tournament
from .models import SignUpForm

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
