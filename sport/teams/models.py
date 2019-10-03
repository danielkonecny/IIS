from django.db import models
from django.conf import settings

# Create your models here.

class Team(models.Model):

    def __str__(self):
        return self.name
    
    flag = models.ImageField(upload_to='flags')
    name = models.CharField(max_length=50,default='Team',unique=True)
   
# requesty hracu o pridani do tymu    
class Request_teamjoin(models.Model):

    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    class Meta:
        unique_together = ["team","user"]

# manageri teamu
class Managers(models.Model):

    def __str__(self):
        return self.user.username

    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        unique_together = ["team","user"]

# hraci jednoho tymu
class Players(models.Model):
    def str__str__(self):
        return self.user.username
    
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)    
    class Meta:
        unique_together = ["team","user"]
    