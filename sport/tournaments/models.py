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

    sponsors = models.ManyToManyField('sponsors.Sponsor', related_name='tour_sponsors',blank=True)   
    teams = models.ManyToManyField('teams.Team', related_name='tour_teams',blank=True)
    requests_teams = models.ManyToManyField('teams.Team', related_name='tour_requests_teams',blank=True)
    rozhodci = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tour_rozhodci',blank=True)
    requests_rozhodci = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tour_requests_rozhodci',blank=True)
    poradatele = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tour_poradatele', on_delete='CASCADE')
    winner = models.ForeignKey('teams.Team', blank=True, null=True, related_name='winner', on_delete=models.CASCADE)
