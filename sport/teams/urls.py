from django.urls import path

from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.index, name='index'),
    path('your_teams/', views.your_teams, name='your_teams'),
    path('<int:id>/',views.single,name='single'),
    
]

