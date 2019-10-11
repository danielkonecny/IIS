from django.shortcuts import get_object_or_404, render
from .models import Team
from tournaments.models import Tournament
from func.func import compare
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q, Count

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
    front = Team.objects.annotate(num_players=Count('players')).filter(num_players__gt=1) # tymy s poctem hracu 1 to umyslne skryva, takove tymy jsou bud nekompletni nebo singleplayerove
    
    return render(request, 'teams/index.html', {'front':front})

@login_required
def your_teams(request):
	user = get_object_or_404(User,pk=request.user.id)
	front = Team.objects.filter(Q(managers=user), Q(players__in=[user])) # vem tymy kde to ridi nebo v nich hraje
	return render(request, 'teams/index.html', {'front':front})
