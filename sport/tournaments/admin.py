from django.contrib import admin

from .models import Tournament, Tournament_teams, Tournament_sponsors, Rozhodci, Poradatele, Request_tournamentjoin, Request_rozhodci
admin.site.register(Tournament)

class Tournament_teamsAdmin(admin.ModelAdmin):
	list_display = ('team','turnaj')
admin.site.register(Tournament_teams, Tournament_teamsAdmin)

class Tournament_sponsorsAdmin(admin.ModelAdmin):
	list_display = ('sponsor','turnaj')
admin.site.register(Tournament_sponsors, Tournament_sponsorsAdmin)

class RozhodciAdmin(admin.ModelAdmin):
	list_display = ('user','turnaj')
admin.site.register(Rozhodci, RozhodciAdmin)

class PoradateleAdmin(admin.ModelAdmin):
	list_display = ('user','turnaj')
admin.site.register(Poradatele, PoradateleAdmin)

class Request_rozhodciAdmin(admin.ModelAdmin):
	list_display = ('user','turnaj')
admin.site.register(Request_rozhodci, Request_rozhodciAdmin)

class Request_tournamentjoinAdmin(admin.ModelAdmin):
	list_display = ('team','turnaj')
admin.site.register(Request_tournamentjoin, Request_tournamentjoinAdmin)
