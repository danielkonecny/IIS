from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # /tournaments/
    path('<int:name>/',views.single,name='detail'), # /tournaments/25/
    
]

