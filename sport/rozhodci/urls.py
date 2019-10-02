from django.urls import path

from . import views

app_name = 'rozhodci'

urlpatterns = [
    path('<int:id>/',views.single,name='single'),
]

