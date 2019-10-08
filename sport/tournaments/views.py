from django.shortcuts import get_object_or_404, render
from .models import Tournament
from teams.models import Team
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from func.func import compare


def single(request,id):
    tournament = get_object_or_404(Tournament,pk=id)
    
    teams = tournament.teams.all()
    rozhodci = tournament.rozhodci.all()
    sponsors = tournament.sponsors.all()

    # vyber vsechny tymy ktere user managuje
    managing_teams = Team.objects.filter(managers=request.user)
    permitted_add = False
    available_teams = None
    if not tournament.started:
        permitted_add = not compare(managing_teams,teams) # pokud jeste nezacal, zkus jestli ma uzivatel moznost se registrovat
    if not permitted_add: # nenaslo to konfliktni teamy, tzn. vytvor seznam tymu ktere muze pridat do turnaje
        available_teams = managing_teams.objects.exclude(tour_teams__in=[tournament]) 

    # vyber vsechny tymy, ve kterych je aktualni user
    his_teams = Team.objects.filter(players__in=[request.user])

    # zjisti jestli muze byt rozhodcim
    permitted = not compare(his_teams, teams)

    return render(request, 'tournaments/single.html', {'tournament': tournament, 'teams':teams,'sponsors': sponsors,'rozhodci':rozhodci,'permitted':permitted,'permitted_add':permitted_add,'available_teams':available_teams})

def index(request):
    front = Tournament.objects.all()
    
    return render(request, 'tournaments/index.html', {'front':front})

@login_required
def your_tournaments(request):
	user = get_object_or_404(User,pk=request.user.id)
	front = Tournament.objects.filter(poradatele=user)
	return render(request, 'tournaments/index.html', {'front':front})
