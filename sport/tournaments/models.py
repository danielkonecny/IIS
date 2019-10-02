from django.db import models

class Tournament(models.Model):

	def __str__(self):
		return self.name

	entry = models.IntegerField(default=0) # poplatek
	player_count = models.IntegerField(default=8) # pocet hracu turnaje (omezit na 2 * 2^n, >= 1)
	started = models.BooleanField(default=False) # pokud turnaj zacne, nejde smazat
	name = models.CharField(max_length=50,default='Tournament') # nazev turnaje
	sport = models.ForeignKey('sports.Sport',on_delete=models.CASCADE) # id sportu turnaje
	singleplayer = models.BooleanField(default=False) # pouze pro solo uzivatele, ne pro tymy
    
