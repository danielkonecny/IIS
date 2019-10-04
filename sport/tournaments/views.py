from django.shortcuts import get_object_or_404, render
from .models import Tournament

def single(request,id):
    tournament = get_object_or_404(Tournament,pk=id)
	
    teams = tournament.teams.all()
    rozhodci = tournament.rozhodci.all()
    
    return render(request, 'tournaments/single.html', {'tournament': tournament, 'teams':teams,'rozhodci':rozhodci})

def index(request):
	front = Tournament.objects.all()
	
	return render(request, 'tournaments/index.html', {'front':front})
