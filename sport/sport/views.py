from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def index(request):

    return render(request, 'index.html')

def logout_request(request):
	logout(request)
	messages.info(request, "You have been logged out.")
	return redirect('index')
