from django.urls import path, re_path

from . import views

app_name = 'forms'

urlpatterns = [
    path('signup',views.signup,name='signup'), 
    path('profile',views.profile,name='profile'), 
    
    re_path(r'^request_player_remove(?P<id>\w+)/(?P<subid>\w+)/$', views.request_player_remove, name='request_player_remove'),
    re_path(r'^request_player_ok(?P<id>\w+)/(?P<subid>\w+)/$', views.request_player_ok, name='request_player_ok'),
       
    re_path(r'^request_team_remove(?P<id>\w+)/(?P<subid>\w+)/$', views.request_team_remove, name='request_team_remove'),
    re_path(r'^request_team_ok(?P<id>\w+)/(?P<subid>\w+)/$', views.request_team_ok, name='request_team_ok'),
    
    re_path(r'^request_rozhodci_remove(?P<id>\w+)/(?P<subid>\w+)/$', views.request_rozhodci_remove, name='request_rozhodci_remove'),
    re_path(r'^request_rozhodci_ok(?P<id>\w+)/(?P<subid>\w+)/$', views.request_rozhodci_ok, name='request_rozhodci_ok'),
 
    re_path(r'^request_add_rozhodci(?P<id>\w+)/(?P<subid>\w+)/$', views.request_add_rozhodci, name='request_add_rozhodci'),
    
    re_path(r'^request_add_player(?P<id_t>\w+)/(?P<id_u>\w+)/$', views.request_add_player, name='request_add_player'),
    
    re_path(r'^remove_player(?P<id>\w+)/(?P<subid>\w+)/$', views.remove_player, name='remove_player'),
    re_path(r'^remove_sponsor(?P<id>\w+)/(?P<subid>\w+)/$', views.remove_sponsor, name='remove_sponsor'),
    re_path(r'^remove_rozhodci(?P<id>\w+)/(?P<subid>\w+)/$', views.remove_rozhodci, name='remove_rozhodci'),
    re_path(r'^remove_team(?P<id>\w+)/(?P<subid>\w+)/$', views.remove_team, name='remove_team'),

    re_path(r'^delete_tournament(?P<id>\w+)/$', views.delete_tournament, name='delete_tournament'),
    re_path(r'^delete_team(?P<id>\w+)/$', views.delete_team, name='delete_team'),
    re_path(r'^edit_tournament(?P<id>\w+)/$', views.edit_tournament, name='edit_tournament'),
    re_path(r'^create_tournament$', views.create_tournament, name='create_tournament'),
    re_path(r'^create_team$', views.create_team, name='create_team'),
    re_path(r'^create_sponsor$', views.create_sponsor, name='create_sponsor'),

    re_path(r'^add_match_results(?P<id>\w+)/$', views.add_match_results, name='add_match_results'),
]

