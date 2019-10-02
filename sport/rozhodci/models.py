from django.db import models
from django.conf import settings

class Rozhodci(models.Model):

	turnaj = models.ForeignKey('tournaments.Tournament',on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
