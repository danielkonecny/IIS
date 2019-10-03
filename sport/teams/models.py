from django.db import models
from django.conf import settings

# Create your models here.

class Team(models.Model):

	def __str__(self):
		return self.name
	
	flag = models.ImageField(upload_to='flags') # ?
	name = models.CharField(max_length=50,default='Team')
   
# requesty hracu o pridani do tymu    
class Request_teamjoin(models.Model):

	team = models.ForeignKey(Team,on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

# manageri teamu
class Managers(models.Model):

	def __str__(self):
		return self.user.username

	team = models.ForeignKey(Team,on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
