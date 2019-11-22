from django.shortcuts import get_object_or_404, render, redirect
from .models import Tournament
from teams.models import Team
from sponsors.models import Sponsor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator

from func.func import compare
from forms.forms import AddTeamForm
from forms.forms import AddSponsorForm

def single(request,id):

    tournament = get_object_or_404(Tournament,pk=id)
    
    teams = tournament.teams.all()
    rozhodci = tournament.rozhodci.all()
    sponsors = tournament.sponsors.all()

    aviable_sponsors = Sponsor.objects.all()
    aviable_sponsors = aviable_sponsors.exclude(tour_sponsors__in=[tournament])

    add_new_team = None # formular na pridani tymu do turnaje
    add_new_sponsor = None  # formular na pridani tymu do turnaje

    # vyber vsechny tymy ktere user managuje
    managing_teams = Team.objects.filter(managers=request.user)
    available_teams = None
    permitted_add_team = False
    permitted_add_sponsor = False
    if not tournament.started:
        available_teams = managing_teams.exclude(tour_teams__in=[tournament])
        available_teams = available_teams.exclude(tour_requests_teams__in=[tournament])
        available_teams = available_teams.filter(singleplayerteam=tournament.singleplayer)

    # ZACINA VALIDACE FORMULARE NA PRIDANI TYMU DO TURNAJE    
    if request.method == 'POST':
        add_new_team = AddTeamForm(request.POST,t=available_teams)
        if add_new_team.is_valid():
            team = add_new_team.cleaned_data['teams']
            tournament.requests_teams.add(team)
        
            return redirect('forms:profile')

    # ZACINA VALIDACE FORMULARE NA PRIDANI SPONSORA DO TURNAJE
    if request.method == 'POST':
        add_new_sponsor = AddSponsorForm(request.POST, s=aviable_sponsors)
        if add_new_sponsor.is_valid():
            sponsors = add_new_sponsor.cleaned_data['sponsors']
            tournament.sponsors.add(sponsors)

            return redirect('forms:profile')

        
    if len(available_teams):
        add_new_team = AddTeamForm(t=available_teams) # vytvor formular na pridani tymu do turnaje, az tedka
        permitted_add_team = True

    if len(aviable_sponsors):
        add_new_sponsor = AddSponsorForm(s=aviable_sponsors) # vytvor formular na pridani tymu do turnaje, az tedka
        permitted_add_sponsor = True

    # vyber vsechny tymy, ve kterych je aktualni user
    his_teams = Team.objects.filter(players__in=[request.user])

    # zjisti jestli muze byt rozhodcim
    permitted = not compare(his_teams, teams)
    
    return render(request, 'tournaments/single.html', {'tournament': tournament, 'teams': teams,'sponsors': sponsors,
                                                       'rozhodci': rozhodci,'permitted': permitted,
                                                       'permitted_add_team': permitted_add_team,
                                                       'permitted_add_sponsor': permitted_add_sponsor,
                                                       'add_new_team': add_new_team, 'add_new_sponsor': add_new_sponsor})
    
def index(request):
    front = Tournament.objects.all()
    paginator = Paginator(front, 10)
    page = request.GET.get('page')  
    content = paginator.get_page(page)
    return render(request, 'tournaments/index.html', {'front':content})

@login_required
def your_tournaments(request):
    user = get_object_or_404(User,pk=request.user.id)
    front = Tournament.objects.filter(poradatele=user)
    return render(request, 'tournaments/index.html', {'front':front})
