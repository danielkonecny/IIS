from django.shortcuts import get_object_or_404, render
from .models import Sponsor
from django.core.paginator import Paginator


def single(request,id):
    sponsor = get_object_or_404(Sponsor,pk=id)
    return render(request, 'sponsors/single.html', {'sponsor': sponsor})

def index(request):
    front = Sponsor.objects.all()
    paginator = Paginator(front, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'sponsors/index.html', {'front': content})
