from django.shortcuts import get_object_or_404, render
from .models import Rozhodci


def single(request,id):
    rozhodci = get_object_or_404(Rozhodci,pk=id)
    return render(request, 'rozhodci/single.html', {'rozhodci': rozhodci})
