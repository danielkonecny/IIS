from django.shortcuts import get_object_or_404, render
from .models import Match


def single(request, id):
    match = get_object_or_404(Match, pk=id)
    return render(request, 'matches/single.html', {'match': match})


def index(request):
    front = Match.objects.all()
    return render(request, 'matches/index.html', {'front': front})
