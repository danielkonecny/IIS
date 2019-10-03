from django.db import models

class Match(models.Model):

	def __str__(self):
		return self.team_A.name + ' vs. ' + self.team_B.name

	turnaj = models.ForeignKey('tournaments.Tournament',on_delete=models.CASCADE)
	team_A = models.ForeignKey('teams.Team', related_name='team_A', on_delete=models.CASCADE)
	team_B = models.ForeignKey('teams.Team',related_name='team_B', on_delete=models.CASCADE)
	start_position = models.IntegerField(default=8)
	finished = models.BooleanField(default=False)
	
class MatchResult(models.Model):

	zapas = models.ForeignKey(Match,on_delete=models.CASCADE)
	score_A = models.IntegerField(default=0)
	score_B = models.IntegerField(default=0)
	score_optional = models.IntegerField(default=0)
	
    
