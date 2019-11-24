from django.db import models


class Match(models.Model):

    def __str__(self):
        return str(self.id)
        # return str(self.team_A.name) + ' vs. ' + str(self.team_B.name)

    turnaj = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE)
    team_A = models.ForeignKey('teams.Team', blank=True, null=True, related_name='team_A', on_delete=models.CASCADE)
    team_B = models.ForeignKey('teams.Team', blank=True, null=True, related_name='team_B', on_delete=models.CASCADE)
    start_position = models.IntegerField(default=8, blank=True)
    finished = models.BooleanField(default=False)
    next_match = models.ForeignKey('matches.Match', blank=True, null=True, on_delete=models.CASCADE)
    score_A = models.IntegerField(default=0)
    score_B = models.IntegerField(default=0)
    # score_optional = models.IntegerField(default=0, blank=True)
    #
    # class Meta:
    #     unique_together = ["team_A", "turnaj", "team_B"]