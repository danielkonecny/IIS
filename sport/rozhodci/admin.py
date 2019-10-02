from django.contrib import admin

from .models import Rozhodci
#admin.site.register(Rozhodci)

class RozhodciAdmin(admin.ModelAdmin):
	list_display = ('user','turnaj')

admin.site.register(Rozhodci, RozhodciAdmin)
