from django import forms
from teams.models import Team
from django.forms import ModelForm

# formular pridani teamu do turnaje
class AddTeamForm(forms.Form):

    teams = forms.ModelChoiceField(queryset=Team.objects.all()) # tohle je prvek formulare OPRAVIT NA NECO ROZUMNYHO

    def __init__(self,*args,**kwargs): # custom konstrukce formulare
        t = kwargs.pop('t') # vytahni z argumentu aktualni request
        super(AddTeamForm,self).__init__(*args,**kwargs) # defualtni konstruktor

        if len(t):
            self.fields['teams'].queryset = t # pristup pres self.fields do vsech prvku formulare POUZE!!!!!
            self.fields['teams'].label = 'Select team:'

class CreateTeam(ModelForm):
    class Meta:
        model = Team
        fields = ['id', 'name','flag'] # pridani noveho tymu

#class TournamentForm(ModelForm):
#    class Meta:
#        model = Team # DOPLNIT FIELDS!
#        fields = ['entry', 'name','player_count', 'started', 'sport','singleplayer'] # pridani / edit turnaje
