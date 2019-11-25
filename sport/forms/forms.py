from django import forms
from teams.models import Team
from django.forms import ModelForm
from tournaments.models import Tournament
from sponsors.models import Sponsor
from matches.models import Match


# formular pridani teamu do turnaje
class AddTeamForm(forms.Form):
    teams = forms.ModelChoiceField(
        queryset=Team.objects.all())  # tohle je povinnej prvek formulare, OPRAVIT NA NECO ROZUMNYHO

    def __init__(self, *args, **kwargs):  # custom konstrukce formulare
        t = kwargs.pop('t')  # vytahni z argumentu aktualni request
        super(AddTeamForm, self).__init__(*args, **kwargs)  # defualtni konstruktor

        if len(t):
            self.fields['teams'].queryset = t  # pristup pres self.fields do vsech prvku formulare POUZE!!!!!
            self.fields['teams'].label = 'Select team:'


class AddSponsorForm(forms.Form):
    sponsors = forms.ModelChoiceField(
        queryset=Sponsor.objects.all())  # tohle je povinnej prvek formulare, OPRAVIT NA NECO ROZUMNYHO

    def __init__(self, *args, **kwargs):  # custom konstrukce formulare
        s = kwargs.pop('s')  # vytahni z argumentu aktualni request
        super(AddSponsorForm, self).__init__(*args, **kwargs)  # defualtni konstruktor

        if len(s):
            self.fields['sponsors'].queryset = s  # pristup pres self.fields do vsech prvku formulare POUZE!!!!!
            self.fields['sponsors'].label = 'Select sponsor:'


class CreateTeam(ModelForm):
    class Meta:
        model = Team
        fields = ['id', 'name', 'flag', 'singleplayerteam']  # pridani noveho tymu


class CreateTournament(ModelForm):
    class Meta:
        model = Tournament
        fields = ['id', 'name', 'sport', 'singleplayer', 'entry', 'player_count']  # pridani noveho turnaje


class CreateSponsor(ModelForm):
    class Meta:
        model = Sponsor
        fields = ['id', 'name', 'logo']  # pridani noveho sponsora


class TournamentForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'entry', 'player_count', 'singleplayer']  # edit turnaje


class AddMatchResultsForm(ModelForm):
    class Meta:
        model = Match
        fields = ['score_A', 'score_B']  # pridani vysleldku zapasu
