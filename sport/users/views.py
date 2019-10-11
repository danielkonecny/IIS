from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

def single(request,id):

    user = get_object_or_404(User,pk=id)     
    teams = user.team_teams.all()

    return render(request, 'users/single.html', {'user': user,'teams':teams})

def players(request):
    players = get_user_model().objects.filter(team_teams=True)
    paginator = Paginator(players, 10)
    page = request.GET.get('page')  
    content = paginator.get_page(page)
    return render(request, 'users/players.html', {'players':content})

def managers(request):    
    players = get_user_model().objects.filter(team_managers=True)
    paginator = Paginator(players, 10)
    page = request.GET.get('page')  
    content = paginator.get_page(page)
    return render(request, 'users/managers.html', {'players':content})
    
def rozhodci(request):
    players = get_user_model().objects.filter(tour_rozhodci=True)
    paginator = Paginator(players, 10)
    page = request.GET.get('page')  
    content = paginator.get_page(page)
    return render(request, 'users/rozhodci.html', {'players':content})
