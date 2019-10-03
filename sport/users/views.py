from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from teams.models import Team, Players

def single(request,id):
    user = get_object_or_404(User,pk=id)   
    
    ids = Players.objects.filter(user=id).values_list('team', flat=True)    
    teams = Team.objects.filter(id__in=list(ids))

    return render(request, 'users/single.html', {'user': user,'teams':teams})

def index(request):
	front = User.objects.all()[:5]

	return render(request, 'users/index.html', {'front':front})
