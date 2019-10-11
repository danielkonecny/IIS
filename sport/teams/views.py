from django.shortcuts import get_object_or_404, render
from .models import Team
from tournaments.models import Tournament
from func.func import compare
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q #, Count
from django.core.paginator import Paginator

def single(request,id):
    team = get_object_or_404(Team,pk=id)
    
    tournaments = team.tour_teams.all()
    players = team.players.all()
    manager = team.managers
    
    # zjistit jestli zobrazovat delete team tlacitko
    active_tournaments = Tournament.objects.filter(started=True) 
    permitted = not compare(tournaments, active_tournaments)
    
    # zjisti jestli se muze nabidnout do tymu jako hrac
    
    able_to_play = True
    if team.singleplayerteam and team.players.count():
        able_to_play = False
        
    return render(request, 'teams/single.html', {'team': team,'tournaments':tournaments,'players':players,'manager':manager,'permitted':permitted,'able_to_play':able_to_play})

def index(request):
    front = Team.objects.all()
    paginator = Paginator(front, 10)
    page = request.GET.get('page')  
    content = paginator.get_page(page)
    return render(request, 'teams/index.html', {'front':content})

@login_required
def your_teams(request):
	user = get_object_or_404(User,pk=request.user.id)
	front = Team.objects.filter(Q(managers=user), Q(players__in=[user])) # vem tymy kde to ridi nebo v nich hraje
	return render(request, 'teams/index.html', {'front':front})
