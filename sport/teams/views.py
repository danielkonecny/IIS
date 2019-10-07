from django.shortcuts import get_object_or_404, render
from .models import Team
from tournaments.models import Tournament
from func.func import compare

def single(request,id):
    team = get_object_or_404(Team,pk=id)
    
    tournaments = team.tour_teams.all()
    players = team.players.all()
    manager = team.managers
    
    # zjistit jestli zobrazovat delete team tlacitko
    active_tournaments = Tournament.objects.filter(started=True) 
    permitted = not compare(tournaments, active_tournaments)
        
    return render(request, 'teams/single.html', {'team': team,'tournaments':tournaments,'players':players,'manager':manager,'permitted':permitted})

def index(request):
    front = Team.objects.all()

    return render(request, 'teams/index.html', {'front':front})
