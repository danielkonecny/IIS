from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('players/', views.players, name='players'),
    path('<int:id>/',views.single,name='single'),
    
]

