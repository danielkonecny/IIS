from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from teams.models import Team
from django.contrib.auth import get_user_model

def single(request,id):
    user = get_object_or_404(User,pk=id)   
    
 #   ids = Players.objects.filter(user=id).values_list('team', flat=True)    
#    teams = Team.objects.filter(id__in=list(ids))

    return render(request, 'users/single.html', {'user': user})#,'teams':teams})

def players(request):
    
#    ids = Players.objects.values_list('user', flat=True).distinct()

#    result = {}
#    for value in ids:
        #x = Players.objects.filter(user=value).values_list('team', flat=True)
#        print(Players.objects.team.all())
    #print(Players.objects.all())
    
    #    result[value] = Team.objects.filter(id__in=x).values_list('name', flat=True)
    #    value = get_user_model().objects.filter(id=value)

    #for p in Players.objects.all():
    #    print(p)
    #    print(p.team.all())

    #for k in result.keys():
    #    print(k)

    #for v in result.values():    
    #    print(list(v))
    

#value_list = MyModel.objects.
    
    #.all()
    
    return render(request, 'users/players.html', {'players':players})
