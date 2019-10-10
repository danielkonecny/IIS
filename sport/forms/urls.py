from django.urls import path

from . import views

app_name = 'forms'

urlpatterns = [
    path('signup',views.signup,name='signup'), 
    path('profile',views.profile,name='profile'), 
    
    path(r'^request_player_remove(?P<id>\w+)/(?P<subid>\w+)/$', views.request_player_remove, name='request_player_remove'),
    path(r'^request_player_ok(?P<id>\w+)/(?P<subid>\w+)/$', views.request_player_ok, name='request_player_ok'),  
       
    path(r'^request_team_remove(?P<id>\w+)/(?P<subid>\w+)/$', views.request_team_remove, name='request_team_remove'),
    path(r'^request_team_ok(?P<id>\w+)/(?P<subid>\w+)/$', views.request_team_ok, name='request_team_ok'),  
    
    path(r'^request_rozhodci_remove(?P<id>\w+)/(?P<subid>\w+)/$', views.request_rozhodci_remove, name='request_rozhodci_remove'),
    path(r'^request_rozhodci_ok(?P<id>\w+)/(?P<subid>\w+)/$', views.request_rozhodci_ok, name='request_rozhodci_ok'),  
 
    path(r'^request_add_rozhodci(?P<id>\w+)/(?P<subid>\w+)/$', views.request_add_rozhodci, name='request_add_rozhodci'), 
    
    path(r'^request_add_player(?P<id>\w+)/(?P<subid>\w+)/$', views.request_add_player, name='request_add_player'),   
    
    path(r'^remove_player(?P<id>\w+)/(?P<subid>\w+)/$', views.remove_player, name='remove_player'),
    path(r'^remove_sponsor(?P<id>\w+)/(?P<subid>\w+)/$', views.remove_sponsor, name='remove_sponsor'),
    path(r'^remove_rozhodci(?P<id>\w+)/(?P<subid>\w+)/$', views.remove_rozhodci, name='remove_rozhodci'),
    path(r'^remove_team(?P<id>\w+)/(?P<subid>\w+)/$', views.remove_team, name='remove_team'),

    path(r'^delete_tournament(?P<id>\w+)/$', views.delete_tournament, name='delete_tournament'),
    path(r'^delete_team(?P<id>\w+)/$', views.delete_team, name='delete_team'),
    
]

