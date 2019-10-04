from django.shortcuts import get_object_or_404, render
from .models import Tournament
from teams.models import Team

def single(request,id):
    tournament = get_object_or_404(Tournament,pk=id)
	
    teams = tournament.teams.all()

    
    return render(request, 'tournaments/single.html', {'tournament': tournament, 'teams':teams})

def index(request):
	front = Tournament.objects.all()
	
	return render(request, 'tournaments/index.html', {'front':front})
