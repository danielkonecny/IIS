from django.contrib import admin

from .models import Team, Request_teamjoin, Managers, Players
admin.site.register(Team)

class Request_teamjoinAdmin(admin.ModelAdmin):
	list_display = ('team','user')
admin.site.register(Request_teamjoin, Request_teamjoinAdmin)

class ManagersAdmin(admin.ModelAdmin):
	list_display = ('team','user')
admin.site.register(Managers, ManagersAdmin)

class PlayersAdmin(admin.ModelAdmin):
	list_display = ('team','user')
#admin.site.register(Players, PlayersAdmin)
