from django.shortcuts import get_object_or_404, render
from .models import Tournament


def single(request,id):
    tournament = get_object_or_404(Tournament,pk=id)
    return render(request, 'tournaments/single.html', {'tournament': tournament})

def index(request):
	front = Tournament.objects.all()[:5]
	
	context = {
		'front': front,
	}
	return render(request, 'tournaments/index.html', context)
