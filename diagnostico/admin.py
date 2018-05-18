from django.contrib import admin
from .models import Relatorio

class RelatorioAdmin(admin.ModelAdmin): #deixar pagina admin mais amigavel
	list_display = ['titulo', 'texto'] 
	search_display = ['titulo']
	#list_filter = ['created', 'modified']

admin.site.register(Relatorio, RelatorioAdmin)

