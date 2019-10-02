from django.db import models

# Create your models here.

class Tournament(models.Model):

	def __str__(self):
		return self.name

	entry = models.IntegerField(default=0)
	player_count = models.IntegerField(default=8)
	started = models.BooleanField(default=False)
	name = models.CharField(max_length=50,default='Tournament')
