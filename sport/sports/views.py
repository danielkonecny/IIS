from django.shortcuts import get_object_or_404, render
from .models import Sport


def single(request,id):
    sport = get_object_or_404(Sport,pk=id)
    return render(request, 'sports/single.html', {'sport': sport})

def index(request):
	front = Sport.objects.all()[:5]
	
	context = {
		'front': front,
	}
	return render(request, 'sports/index.html', context)
