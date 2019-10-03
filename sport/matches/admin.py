from django.contrib import admin

# Register your models here.

from .models import Match, MatchResult

class MatchAdmin(admin.ModelAdmin):
	list_display = ('turnaj','team_A','team_B')

class MatchResultAdmin(admin.ModelAdmin):
	list_display = ('zapas','score_A','score_B')

admin.site.register(MatchResult, MatchResultAdmin)
admin.site.register(Match, MatchAdmin)
