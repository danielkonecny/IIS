from django.shortcuts import get_object_or_404, render
from .models import Team
from tournaments.models import Tournament

def single(request,id):
    team = get_object_or_404(Team,pk=id)
    
    tournaments = team.tour_teams.all()
    players = team.players.all()
    manager = team.managers
        
    return render(request, 'teams/single.html', {'team': team, 'tournaments':tournaments, 'players':players,'manager':manager})

def index(request):
	front = Team.objects.all()

	return render(request, 'teams/index.html', {'front':front})
