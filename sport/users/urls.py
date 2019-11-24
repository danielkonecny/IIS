from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # path('players/', views.players, name='players'),
    path('<int:id>/', views.single, name='single'),
    # path('managers/', views.managers, name='managers'),
    # path('rozhodci/', views.rozhodci, name='rozhodci'),
    path('all/', views.all, name='all'),

]
