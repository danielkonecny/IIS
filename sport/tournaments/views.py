from django.shortcuts import get_object_or_404, render, redirect
from .models import Tournament
from teams.models import Team
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

from func.func import compare
from forms.forms import AddTeamForm

def single(request,id):

    tournament = get_object_or_404(Tournament,pk=id)
    
    teams = tournament.teams.all()
    rozhodci = tournament.rozhodci.all()
    sponsors = tournament.sponsors.all()

    add_new = None # formular na pridani tymu do turnaje

    # vyber vsechny tymy ktere user managuje
    managing_teams = Team.objects.filter(managers=request.user)
    available_teams = None
    permitted_add = False
    if not tournament.started:
        available_teams = managing_teams.exclude(Q(tour_teams__in=[tournament]))
        available_teams = available_teams.exclude(Q(tour_requests_teams__in=[tournament]))

    print(available_teams)

    # ZACINA VALIDACE FORMULARE NA PRIDANI TYMU DO TURNAJE    
    if request.method == 'POST':
        add_new = AddTeamForm(request.POST,t=available_teams)
        if add_new.is_valid():
            team = add_new.cleaned_data['teams']
            tournament.requests_teams.add(team)
        
            return redirect('forms:profile')
        
    if len(available_teams):
        add_new = AddTeamForm(t=available_teams) # vytvor formular na pridani tymu do turnaje, az tedka
        permitted_add = True

    # vyber vsechny tymy, ve kterych je aktualni user
    his_teams = Team.objects.filter(players__in=[request.user])

    # zjisti jestli muze byt rozhodcim
    permitted = not compare(his_teams, teams)
    
    return render(request, 'tournaments/single.html', {'tournament': tournament, 'teams':teams,'sponsors': sponsors,'rozhodci':rozhodci,'permitted':permitted,'permitted_add':permitted_add,'add_new':add_new})
    
def index(request):
    front = Tournament.objects.all()
    
    return render(request, 'tournaments/index.html', {'front':front})

@login_required
def your_tournaments(request):
    user = get_object_or_404(User,pk=request.user.id)
    front = Tournament.objects.filter(poradatele=user)
    return render(request, 'tournaments/index.html', {'front':front})
