from django.db import models

# Create your models here.

class Sponsor(models.Model):

	def __str__(self):
		return self.name
		
	logo = models.ImageField(upload_to='logos',blank=True)
	name = models.CharField(max_length=50,default='Sponsor',unique=True)
    
