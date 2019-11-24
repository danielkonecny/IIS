from django.contrib import admin

# Register your models here.

from .models import Match


class MatchAdmin(admin.ModelAdmin):
    list_display = ('turnaj', 'team_A', 'team_B', 'score_A', 'score_B', 'start_position', 'next_match')


admin.site.register(Match, MatchAdmin)
