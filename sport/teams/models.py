from django.db import models
from django.conf import settings

class Team(models.Model):

    def __str__(self):
        return self.name
    
    flag = models.ImageField(upload_to='pic_folder/', default = 'pic_folder/None/no-img.jpg',blank=True)
    name = models.CharField(max_length=50,default='Team',unique=True)
    players = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='team_teams',blank=True)
    managers = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='team_managers', on_delete='CASCADE')
    requests_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='team_requests_users',blank=True)
    singleplayerteam = models.BooleanField(default=False)
