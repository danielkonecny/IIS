from django.db import models

# Create your models here.

class Sport(models.Model):

	def __str__(self):
		return self.name
		
	name = models.CharField(max_length=50,default='Sport', unique=True)
    
