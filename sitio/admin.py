from django.contrib import admin
from .models import Question, Control, Dados, Contadores, Description

class QuestionAdmin(admin.ModelAdmin): #deixar pagina admin mais amigavel
	list_display = ['id', 'text'] 
	search_display = ['id']
	list_filter = ['created', 'modified']

admin.site.register(Question, QuestionAdmin)

class ControlAdmin(admin.ModelAdmin): #deixar pagina admin mais amigavel
	list_display = ['id', 'identificador'] 
	search_display = ['id']
	list_filter = ['identificador']
	
admin.site.register(Control, ControlAdmin)

class DadosAdmin(admin.ModelAdmin): #deixar pagina admin mais amigavel
	list_display = ['id_usuario', 'email_usuario', 'media_Financeiro_Estrutural','media_Marketing','media_Pessoas_Processos',
	'nivel_Financeiro_Estrutural','nivel_Marketing', 'nivel_Pessoas_Processos', 'resposta_pergunta_1', 'resposta_pergunta_2','resposta_pergunta_3','resposta_pergunta_4', 'resposta_pergunta_5',
 	'resposta_pergunta_6', 'resposta_pergunta_7', 'resposta_pergunta_8', 'resposta_pergunta_9', 
 	'resposta_pergunta_10', 'resposta_pergunta_11', 'resposta_pergunta_12']
	search_display = ['id_usuario']
	list_filter = ['id_usuario']
	
admin.site.register(Dados, DadosAdmin)

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['message_form', 'message_register']
    search_display = ['id']
    list_filter = ['message_form']
    
admin.site.register(Description, DescriptionAdmin)


class ContadoresAdmin(admin.ModelAdmin): #deixar pagina admin mais amigavel
	list_display = ['id','num_financeiro_estrutural_nivel_1','num_financeiro_estrutural_nivel_2',
	'num_financeiro_estrutural_nivel_3','num_marketing_nivel_1', 'num_marketing_nivel_2', 
	'num_marketing_nivel_3', 'num_pessoas_processos_nivel_1',
	'num_pessoas_processos_nivel_2', 'num_pessoas_processos_nivel_3'] 
	search_display = ['id']
	list_filter = ['id']
	
admin.site.register(Contadores, ContadoresAdmin)

