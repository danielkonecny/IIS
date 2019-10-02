from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Tournament


def single(request,name):
    return HttpResponse("Tournament detail, name: %s" % name)


def index(request):
	front = Tournament.objects.all()[:5]
	output = ', '.join([t.name for t in front])
	return HttpResponse(output)
