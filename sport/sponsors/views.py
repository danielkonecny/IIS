from django.shortcuts import get_object_or_404, render
from .models import Sponsor


def single(request,id):
    sponsor = get_object_or_404(Sponsor,pk=id)
    return render(request, 'sponsors/single.html', {'sponsor': sponsor})

def index(request):
	front = Sponsor.objects.all()[:5]
	
	return render(request, 'sponsors/index.html', {'front':front})
