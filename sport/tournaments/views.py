from django.shortcuts import get_object_or_404, render
from .models import Tournament
from teams.models import Team

from func.func import compare


def single(request,id):
    tournament = get_object_or_404(Tournament,pk=id)
    
    teams = tournament.teams.all()
    rozhodci = tournament.rozhodci.all()

    # vyber vsechny tymy, ve kterych je aktualni user
    his_teams = Team.objects.filter(players__in=[request.user.id])

    # zjisti jestli muze byt rozhodcim
    permitted = not compare(his_teams, teams) 

    return render(request, 'tournaments/single.html', {'tournament': tournament, 'teams':teams,'rozhodci':rozhodci,'permitted':permitted})

def index(request):
    front = Tournament.objects.all()
    
    return render(request, 'tournaments/index.html', {'front':front})
