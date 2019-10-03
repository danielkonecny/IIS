from django.db import models
from django.conf import settings

# jeden turnaj
class Tournament(models.Model):

	def __str__(self):
		return self.name

	entry = models.IntegerField(default=0) # poplatek
	player_count = models.IntegerField(default=8) # pocet hracu turnaje (omezit na 2 * 2^n, >= 1)
	started = models.BooleanField(default=False) # pokud turnaj zacne, nejde smazat
	name = models.CharField(max_length=50,default='Tournament') # nazev turnaje
	sport = models.ForeignKey('sports.Sport',on_delete=models.CASCADE) # id sportu turnaje
	singleplayer = models.BooleanField(default=False) # pouze pro solo uzivatele, ne pro tymy
    
# teamy co jsou soucasti jednoho turnaje
class Tournament_teams(models.Model):

	turnaj = models.ForeignKey(Tournament,on_delete=models.CASCADE)
	team = models.ForeignKey('teams.Team',on_delete=models.CASCADE)

# sponzori jednoho turnaje	
class Tournament_sponsors(models.Model):

	turnaj = models.ForeignKey(Tournament,on_delete=models.CASCADE)
	sponsor = models.ForeignKey('sponsors.Sponsor',on_delete=models.CASCADE)

# rozhodci jednoho turnaje
class Rozhodci(models.Model):

	turnaj = models.ForeignKey(Tournament,on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	
# requesty teamu o hru v turnaji
class Request_tournamentjoin(models.Model):

	turnaj = models.ForeignKey('tournaments.Tournament',on_delete=models.CASCADE)
	team = models.ForeignKey('teams.Team',on_delete=models.CASCADE)

# request uzivatele o roli rozhodciho turnaje
class Request_rozhodci(models.Model):

	turnaj = models.ForeignKey(Tournament,on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

# poradatele turnaju
class Poradatele(models.Model):

	turnaj = models.ForeignKey(Tournament,on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
