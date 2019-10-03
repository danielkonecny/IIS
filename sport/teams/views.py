from django.shortcuts import get_object_or_404, render
from .models import Team


def single(request,id):
    team = get_object_or_404(Team,pk=id)
    return render(request, 'teams/single.html', {'team': team})

def index(request):
	front = Team.objects.all()[:5]

	return render(request, 'teams/index.html', {'front':front})
