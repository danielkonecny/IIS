from django.urls import path

from . import views

app_name = 'tournaments'

urlpatterns = [
    path('', views.index, name='index'), # /tournaments/
    path('your_tournaments/',views.your_tournaments, name='your_tournaments'),
    path('<int:id>/',views.single,name='single'), # /tournaments/25/
    
]

