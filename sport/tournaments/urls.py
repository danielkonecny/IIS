from django.urls import path, re_path

from . import views

app_name = 'tournaments'

urlpatterns = [
    path('', views.index, name='index'), # /tournaments/
    path('your_tournaments/',views.your_tournaments, name='your_tournaments'),
    path('<int:id>/',views.single,name='single'), # /tournaments/25/
    re_path(r'^(?P<id>\w+)/match_schedule$', views.start_tournament, name='start_tournament'),
    # path('<int:id>/match_schedule',views.start_tournament(),name='start_tournament'), # /tournaments/25/match_schedule
    
]

