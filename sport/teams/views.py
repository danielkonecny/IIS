from django.shortcuts import get_object_or_404, render
from .models import Team, Players, Managers
from tournaments.models import Tournament, Tournament_teams
from django.contrib.auth import get_user_model

def single(request,id):
    team = get_object_or_404(Team,pk=id)
    
    ids = Tournament_teams.objects.filter(team=id).values_list('turnaj', flat=True)
    tournaments = Tournament.objects.filter(id__in=list(ids))
    
    ids = Managers.objects.filter(team=id).values_list('id', flat=True)
    managers = get_user_model().objects.filter(id__in=list(ids))
    
    ids = Players.objects.filter(team=id).values_list('id', flat=True)
    players = get_user_model().objects.filter(id__in=list(ids))
    
    return render(request, 'teams/single.html', {'team': team, 'tournaments':tournaments, 'players':players, 'managers':managers})

def index(request):
	front = Team.objects.all()[:5]

	return render(request, 'teams/index.html', {'front':front})
