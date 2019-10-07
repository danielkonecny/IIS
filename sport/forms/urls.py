from django.urls import path

from . import views

app_name = 'forms'

urlpatterns = [
    path('signup',views.signup,name='signup'), 
    path('profile',views.profile,name='profile'), 
    
    path(r'^request_player_remove(?P<id>\w+)/(?P<subid>\w+)/', views.request_player_remove, name='request_player_remove'),
    path(r'^request_player_ok(?P<id>\w+)/(?P<subid>\w+)/', views.request_player_ok, name='request_player_ok'),  
       
    path(r'^request_team_remove(?P<id>\w+)/(?P<subid>\w+)/', views.request_team_remove, name='request_team_remove'),
    path(r'^request_team_ok(?P<id>\w+)/(?P<subid>\w+)/', views.request_team_ok, name='request_team_ok'),  
    
    path(r'^request_rozhodci_remove(?P<id>\w+)/(?P<subid>\w+)/', views.request_rozhodci_remove, name='request_rozhodci_remove'),
    path(r'^request_rozhodci_ok(?P<id>\w+)/(?P<subid>\w+)/', views.request_rozhodci_ok, name='request_rozhodci_ok'),  
]

