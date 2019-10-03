from django.urls import path

from . import views

app_name = 'sponsors'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/',views.single,name='single'),
    
]

