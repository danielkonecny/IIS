from django.shortcuts import get_object_or_404, render
from .models import Tournament, Tournament_teams
from teams.models import Team

def single(request,id):
    tournament = get_object_or_404(Tournament,pk=id)
    tournament_teams = Tournament_teams.objects.filter(turnaj=id).values_list('team', flat=True)
	
    teams = Team.objects.filter(id__in=list(tournament_teams))

    
    return render(request, 'tournaments/single.html', {'tournament': tournament, 'teams':teams})

def index(request):
	front = Tournament.objects.all()
	
	return render(request, 'tournaments/index.html', {'front':front})
