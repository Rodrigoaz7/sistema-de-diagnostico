from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from sitio.models import Question, Contadores, Dados
from django.db.models import F

#Ajustando o formulário da criação de usuários
class UserAdminCreationForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'name', 'email', 'telefone', 'empresa', 'ramo']

	def media_financeiro_estrutural(self, dict):
		respostas_financeiro_estrutural = 0.0
		cont = 0
		for key in dict:
			if str(Question.objects.get(pk=key).segmentos) == 'Financeiro/Estrutural':
				cont = cont + 1
				respostas_financeiro_estrutural = respostas_financeiro_estrutural + float(dict[key])

		return respostas_financeiro_estrutural/cont

	def media_marketing(self, dict):
		respostas_marketing = 0.0
		cont = 0
		for key in dict:
			if str(Question.objects.get(pk=key).segmentos) == 'Marketing':
				cont = cont + 1
				respostas_marketing = respostas_marketing + float(dict[key])

		return respostas_marketing/cont

	def media_pessoas_processos(self, dict):
		respostas_pessoas_processos = 0.0
		cont = 0
		for key in dict:
			if str(Question.objects.get(pk=key).segmentos) == 'Pessoas/Processos':
				cont = cont + 1
				respostas_pessoas_processos = respostas_pessoas_processos + float(dict[key])

		return respostas_pessoas_processos/cont
	


	def atualizar_media_and_niveis(self, Dados, mediaA, mediaB, mediaC, nivelA, nivelB, nivelC, idt, email, inputs):
		Dados.media_Financeiro_Estrutural = mediaA
		Dados.media_Marketing = mediaB
		Dados.media_Pessoas_Processos = mediaC
		Dados.nivel_Financeiro_Estrutural = nivelA
		Dados.nivel_Marketing = nivelB
		Dados.nivel_Pessoas_Processos = nivelC
		Dados.id_usuario = idt
		Dados.email_usuario = email
		
		for key in inputs:
			if(key == 1): Dados.resposta_pergunta_1 = int(inputs[key])
			elif(key == 2): Dados.resposta_pergunta_2 = int(inputs[key])
			elif(key == 3): Dados.resposta_pergunta_3 = int(inputs[key])
			elif(key == 4): Dados.resposta_pergunta_4 = int(inputs[key])
			elif(key == 5): Dados.resposta_pergunta_5 = int(inputs[key])
			elif(key == 6): Dados.resposta_pergunta_6 = int(inputs[key])
			elif(key == 7): Dados.resposta_pergunta_7 = int(inputs[key])
			elif(key == 8): Dados.resposta_pergunta_8 = int(inputs[key])
			elif(key == 9): Dados.resposta_pergunta_9 = int(inputs[key])
			elif(key == 10): Dados.resposta_pergunta_10 = int(inputs[key])
			elif(key == 11): Dados.resposta_pergunta_11 = int(inputs[key])
			elif(key == 12): Dados.resposta_pergunta_12 = int(inputs[key])


	def atualizar_contadores(self, nivelA, nivelB, nivelC, Dados):
		# Apenas o objeto com o id igual a 1 (Como se trata de contadores, apenas uma linha é necessária)
		contadores = Contadores.objects.get_or_create(pk=1)

		# Usei o update, pois estamos tratando de uma tupla !
		if(nivelA == 1): Contadores.objects.filter(pk=1).update(num_financeiro_estrutural_nivel_1=F('num_financeiro_estrutural_nivel_1')+1)
		elif(nivelA == 2): Contadores.objects.filter(pk=1).update(num_financeiro_estrutural_nivel_2=F('num_financeiro_estrutural_nivel_2')+1)
		else: Contadores.objects.filter(pk=1).update(num_financeiro_estrutural_nivel_3=F('num_financeiro_estrutural_nivel_3')+1)

		if(nivelB == 1): Contadores.objects.filter(pk=1).update(num_marketing_nivel_1=F('num_marketing_nivel_1')+1)
		elif(nivelB == 2): Contadores.objects.filter(pk=1).update(num_marketing_nivel_2=F('num_marketing_nivel_2')+1)
		else: Contadores.objects.filter(pk=1).update(num_marketing_nivel_3=F('num_marketing_nivel_3')+1)

		if(nivelC == 1): Contadores.objects.filter(pk=1).update(num_pessoas_processos_nivel_1=F('num_pessoas_processos_nivel_1')+1)
		elif(nivelC == 2): Contadores.objects.filter(pk=1).update(num_pessoas_processos_nivel_2=F('num_pessoas_processos_nivel_2')+1)
		else: Contadores.objects.filter(pk=1).update(num_pessoas_processos_nivel_3=F('num_pessoas_processos_nivel_3')+1)
		
		# Verificando opções para pergunta 1:
		if(Dados.resposta_pergunta_1 == 1): num_pergunta_1_resposta_1 = Contadores.objects.filter(pk=1).update(num_pergunta_1_resposta_1=F('num_pergunta_1_resposta_1')+1)
		elif(Dados.resposta_pergunta_1 == 2): Contadores.objects.filter(pk=1).update(num_pergunta_1_resposta_2=F('num_pergunta_1_resposta_2')+1)
		elif(Dados.resposta_pergunta_1 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_1_resposta_3=F('num_pergunta_1_resposta_3')+1)
		elif(Dados.resposta_pergunta_1 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_1_resposta_4=F('num_pergunta_1_resposta_4')+1)
		elif(Dados.resposta_pergunta_1 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_1_resposta_5=F('num_pergunta_1_resposta_5')+1)
		elif(Dados.resposta_pergunta_1 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_1_resposta_6=F('num_pergunta_1_resposta_6')+1)
		elif(Dados.resposta_pergunta_1 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_1_resposta_7=F('num_pergunta_1_resposta_7')+1)
		elif(Dados.resposta_pergunta_1 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_1_resposta_8=F('num_pergunta_1_resposta_8')+1)
		elif(Dados.resposta_pergunta_1 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_1_resposta_9=F('num_pergunta_1_resposta_9')+1)
		elif(Dados.resposta_pergunta_1 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_1_resposta_10=F('num_pergunta_1_resposta_10')+1)
			
		# Verificando opções para a pergunta 2: 
		if(Dados.resposta_pergunta_2 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_2_resposta_1=F('num_pergunta_2_resposta_1')+1)
		elif(Dados.resposta_pergunta_2 == 2): 	Contadores.objects.filter(pk=1).update(num_pergunta_2_resposta_2=F('num_pergunta_2_resposta_2')+1)
		elif(Dados.resposta_pergunta_2 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_2_resposta_3=F('num_pergunta_2_resposta_3')+1)
		elif(Dados.resposta_pergunta_2 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_2_resposta_4=F('num_pergunta_2_resposta_4')+1)
		elif(Dados.resposta_pergunta_2 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_2_resposta_5=F('num_pergunta_2_resposta_5')+1)
		elif(Dados.resposta_pergunta_2 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_2_resposta_6=F('num_pergunta_2_resposta_6')+1)
		elif(Dados.resposta_pergunta_2 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_2_resposta_7=F('num_pergunta_2_resposta_7')+1)
		elif(Dados.resposta_pergunta_2 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_2_resposta_8=F('num_pergunta_2_resposta_8')+1)
		elif(Dados.resposta_pergunta_2 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_2_resposta_9=F('num_pergunta_2_resposta_9')+1)
		elif(Dados.resposta_pergunta_2 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_2_resposta_10=F('num_pergunta_2_resposta_10')+1)

		#Verificando opções para a pergunta 3:
		if(Dados.resposta_pergunta_3 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_3_resposta_1=F('num_pergunta_3_resposta_1')+1)
		elif(Dados.resposta_pergunta_3 == 2): 	Contadores.objects.filter(pk=1).update(num_pergunta_3_resposta_2=F('num_pergunta_3_resposta_2')+1)
		elif(Dados.resposta_pergunta_3 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_3_resposta_3=F('num_pergunta_3_resposta_3')+1)
		elif(Dados.resposta_pergunta_3 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_3_resposta_4=F('num_pergunta_3_resposta_4')+1)
		elif(Dados.resposta_pergunta_3 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_3_resposta_5=F('num_pergunta_3_resposta_5')+1)
		elif(Dados.resposta_pergunta_3 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_3_resposta_6=F('num_pergunta_3_resposta_6')+1)
		elif(Dados.resposta_pergunta_3 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_3_resposta_7=F('num_pergunta_3_resposta_7')+1)
		elif(Dados.resposta_pergunta_3 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_3_resposta_8=F('num_pergunta_3_resposta_8')+1)
		elif(Dados.resposta_pergunta_3 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_3_resposta_9=F('num_pergunta_3_resposta_9')+1)
		elif(Dados.resposta_pergunta_3 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_3_resposta_10=F('num_pergunta_3_resposta_10')+1)
			
		# Verificando opções para pergunta 4:
		if(Dados.resposta_pergunta_4 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_4_resposta_1=F('num_pergunta_4_resposta_1')+1)
		elif(Dados.resposta_pergunta_4 == 2): 	Contadores.objects.filter(pk=1).update(num_pergunta_4_resposta_2=F('num_pergunta_4_resposta_2')+1)
		elif(Dados.resposta_pergunta_4 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_4_resposta_3=F('num_pergunta_4_resposta_3')+1)
		elif(Dados.resposta_pergunta_4 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_4_resposta_4=F('num_pergunta_4_resposta_4')+1)
		elif(Dados.resposta_pergunta_4 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_4_resposta_5=F('num_pergunta_4_resposta_5')+1)
		elif(Dados.resposta_pergunta_4 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_4_resposta_6=F('num_pergunta_4_resposta_6')+1)
		elif(Dados.resposta_pergunta_4 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_4_resposta_7=F('num_pergunta_4_resposta_7')+1)
		elif(Dados.resposta_pergunta_4 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_4_resposta_8=F('num_pergunta_4_resposta_8')+1)
		elif(Dados.resposta_pergunta_4 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_4_resposta_9=F('num_pergunta_4_resposta_9')+1)
		elif(Dados.resposta_pergunta_4 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_4_resposta_10=F('num_pergunta_4_resposta_10')+1)
		
		#Verificando opções para a pergunta 5:
		if(Dados.resposta_pergunta_5 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_5_resposta_1=F('num_pergunta_5_resposta_1')+1)
		elif(Dados.resposta_pergunta_5 == 2): 	Contadores.objects.filter(pk=1).update(num_pergunta_5_resposta_2=F('num_pergunta_5_resposta_2')+1)
		elif(Dados.resposta_pergunta_5 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_5_resposta_3=F('num_pergunta_5_resposta_3')+1)
		elif(Dados.resposta_pergunta_5 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_5_resposta_4=F('num_pergunta_5_resposta_4')+1)
		elif(Dados.resposta_pergunta_5 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_5_resposta_5=F('num_pergunta_5_resposta_5')+1)
		elif(Dados.resposta_pergunta_5 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_5_resposta_6=F('num_pergunta_5_resposta_6')+1)
		elif(Dados.resposta_pergunta_5 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_5_resposta_7=F('num_pergunta_5_resposta_7')+1)
		elif(Dados.resposta_pergunta_5 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_5_resposta_8=F('num_pergunta_5_resposta_8')+1)
		elif(Dados.resposta_pergunta_5 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_5_resposta_9=F('num_pergunta_5_resposta_9')+1)
		elif(Dados.resposta_pergunta_5 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_5_resposta_10=F('num_pergunta_5_resposta_10')+1)
		
		#Verificando opções para a pergunta 6:
		if(Dados.resposta_pergunta_6 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_6_resposta_1=F('num_pergunta_6_resposta_1')+1)
		elif(Dados.resposta_pergunta_6 == 2): 	Contadores.objects.filter(pk=1).update(num_pergunta_6_resposta_2=F('num_pergunta_6_resposta_2')+1)
		elif(Dados.resposta_pergunta_6 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_6_resposta_3=F('num_pergunta_6_resposta_3')+1)
		elif(Dados.resposta_pergunta_6 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_6_resposta_4=F('num_pergunta_6_resposta_4')+1)
		elif(Dados.resposta_pergunta_6 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_6_resposta_5=F('num_pergunta_6_resposta_5')+1)
		elif(Dados.resposta_pergunta_6 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_6_resposta_6=F('num_pergunta_6_resposta_6')+1)
		elif(Dados.resposta_pergunta_6 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_6_resposta_7=F('num_pergunta_6_resposta_7')+1)
		elif(Dados.resposta_pergunta_6 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_6_resposta_8=F('num_pergunta_6_resposta_8')+1)
		elif(Dados.resposta_pergunta_6 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_6_resposta_9=F('num_pergunta_6_resposta_9')+1)
		elif(Dados.resposta_pergunta_6 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_6_resposta_10=F('num_pergunta_6_resposta_10')+1)
		
		# Verificando opções para pergunta 7:
		if(Dados.resposta_pergunta_7 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_7_resposta_1=F('num_pergunta_7_resposta_1')+1)
		elif(Dados.resposta_pergunta_7 == 2): Contadores.objects.filter(pk=1).update(num_pergunta_7_resposta_2=F('num_pergunta_7_resposta_2')+1)
		elif(Dados.resposta_pergunta_7 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_7_resposta_3=F('num_pergunta_7_resposta_3')+1)
		elif(Dados.resposta_pergunta_7 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_7_resposta_4=F('num_pergunta_7_resposta_4')+1)
		elif(Dados.resposta_pergunta_7 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_7_resposta_5=F('num_pergunta_7_resposta_5')+1)
		elif(Dados.resposta_pergunta_7 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_7_resposta_6=F('num_pergunta_7_resposta_6')+1)
		elif(Dados.resposta_pergunta_7 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_7_resposta_7=F('num_pergunta_7_resposta_7')+1)
		elif(Dados.resposta_pergunta_7 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_7_resposta_8=F('num_pergunta_7_resposta_8')+1)
		elif(Dados.resposta_pergunta_7 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_7_resposta_9=F('num_pergunta_7_resposta_9')+1)
		elif(Dados.resposta_pergunta_7 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_7_resposta_10=F('num_pergunta_7_resposta_10')+1)
			
		# Verificando opções para a pergunta 8: 
		if(Dados.resposta_pergunta_8 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_8_resposta_1=F('num_pergunta_8_resposta_1')+1)
		elif(Dados.resposta_pergunta_8 == 2): 	Contadores.objects.filter(pk=1).update(num_pergunta_8_resposta_2=F('num_pergunta_8_resposta_2')+1)
		elif(Dados.resposta_pergunta_8 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_8_resposta_3=F('num_pergunta_8_resposta_3')+1)
		elif(Dados.resposta_pergunta_8 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_8_resposta_4=F('num_pergunta_8_resposta_4')+1)
		elif(Dados.resposta_pergunta_8 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_8_resposta_5=F('num_pergunta_8_resposta_5')+1)
		elif(Dados.resposta_pergunta_8 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_8_resposta_6=F('num_pergunta_8_resposta_6')+1)
		elif(Dados.resposta_pergunta_8 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_8_resposta_7=F('num_pergunta_8_resposta_7')+1)
		elif(Dados.resposta_pergunta_8 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_8_resposta_8=F('num_pergunta_8_resposta_8')+1)
		elif(Dados.resposta_pergunta_8 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_8_resposta_9=F('num_pergunta_8_resposta_9')+1)
		elif(Dados.resposta_pergunta_8 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_8_resposta_10=F('num_pergunta_8_resposta_10')+1)

		#Verificando opções para a pergunta 9:
		if(Dados.resposta_pergunta_9 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_9_resposta_1=F('num_pergunta_9_resposta_1')+1)
		elif(Dados.resposta_pergunta_9 == 2): 	Contadores.objects.filter(pk=1).update(num_pergunta_9_resposta_2=F('num_pergunta_9_resposta_2')+1)
		elif(Dados.resposta_pergunta_9 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_9_resposta_3=F('num_pergunta_9_resposta_3')+1)
		elif(Dados.resposta_pergunta_9 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_9_resposta_4=F('num_pergunta_9_resposta_4')+1)
		elif(Dados.resposta_pergunta_9 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_9_resposta_5=F('num_pergunta_9_resposta_5')+1)
		elif(Dados.resposta_pergunta_9 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_9_resposta_6=F('num_pergunta_9_resposta_6')+1)
		elif(Dados.resposta_pergunta_9 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_9_resposta_7=F('num_pergunta_9_resposta_7')+1)
		elif(Dados.resposta_pergunta_9 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_9_resposta_8=F('num_pergunta_9_resposta_8')+1)
		elif(Dados.resposta_pergunta_9 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_9_resposta_9=F('num_pergunta_9_resposta_9')+1)
		elif(Dados.resposta_pergunta_9 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_9_resposta_10=F('num_pergunta_9_resposta_10')+1)
		
		# Verificando as opções para a pergunta 10:
		if(Dados.resposta_pergunta_10 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_10_resposta_1=F('num_pergunta_10_resposta_1')+1)
		elif(Dados.resposta_pergunta_10 == 2): 	Contadores.objects.filter(pk=1).update(num_pergunta_10_resposta_2=F('num_pergunta_10_resposta_2')+1)
		elif(Dados.resposta_pergunta_10 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_10_resposta_3=F('num_pergunta_10_resposta_3')+1)
		elif(Dados.resposta_pergunta_10 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_10_resposta_4=F('num_pergunta_10_resposta_4')+1)
		elif(Dados.resposta_pergunta_10 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_10_resposta_5=F('num_pergunta_10_resposta_5')+1)
		elif(Dados.resposta_pergunta_10 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_10_resposta_6=F('num_pergunta_10_resposta_6')+1)
		elif(Dados.resposta_pergunta_10 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_10_resposta_7=F('num_pergunta_10_resposta_7')+1)
		elif(Dados.resposta_pergunta_10 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_10_resposta_8=F('num_pergunta_10_resposta_8')+1)
		elif(Dados.resposta_pergunta_10 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_10_resposta_9=F('num_pergunta_10_resposta_9')+1)
		elif(Dados.resposta_pergunta_10 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_10_resposta_10=F('num_pergunta_10_resposta_10')+1)
		
		# Verificando as opções para a pergunta 11:
		if(Dados.resposta_pergunta_11 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_11_resposta_1=F('num_pergunta_11_resposta_1')+1)
		elif(Dados.resposta_pergunta_11 == 2): 	Contadores.objects.filter(pk=1).update(num_pergunta_11_resposta_2=F('num_pergunta_11_resposta_2')+1)
		elif(Dados.resposta_pergunta_11 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_11_resposta_3=F('num_pergunta_11_resposta_3')+1)
		elif(Dados.resposta_pergunta_11 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_11_resposta_4=F('num_pergunta_11_resposta_4')+1)
		elif(Dados.resposta_pergunta_11 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_11_resposta_5=F('num_pergunta_11_resposta_5')+1)
		elif(Dados.resposta_pergunta_11 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_11_resposta_6=F('num_pergunta_11_resposta_6')+1)
		elif(Dados.resposta_pergunta_11 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_11_resposta_7=F('num_pergunta_11_resposta_7')+1)
		elif(Dados.resposta_pergunta_11 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_11_resposta_8=F('num_pergunta_11_resposta_8')+1)
		elif(Dados.resposta_pergunta_11 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_11_resposta_9=F('num_pergunta_11_resposta_9')+1)
		elif(Dados.resposta_pergunta_11 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_11_resposta_10=F('num_pergunta_11_resposta_10')+1)
		
		# Verificando as opções para a pergunta 12:
		if(Dados.resposta_pergunta_12 == 1): Contadores.objects.filter(pk=1).update(num_pergunta_12_resposta_1=F('num_pergunta_12_resposta_1')+1)
		elif(Dados.resposta_pergunta_12 == 2): 	Contadores.objects.filter(pk=1).update(num_pergunta_12_resposta_2=F('num_pergunta_12_resposta_2')+1)
		elif(Dados.resposta_pergunta_12 == 3): Contadores.objects.filter(pk=1).update(num_pergunta_12_resposta_3=F('num_pergunta_12_resposta_3')+1)
		elif(Dados.resposta_pergunta_12 == 4): Contadores.objects.filter(pk=1).update(num_pergunta_12_resposta_4=F('num_pergunta_12_resposta_4')+1)
		elif(Dados.resposta_pergunta_12 == 5): Contadores.objects.filter(pk=1).update(num_pergunta_12_resposta_5=F('num_pergunta_12_resposta_5')+1)
		elif(Dados.resposta_pergunta_12 == 6): Contadores.objects.filter(pk=1).update(num_pergunta_12_resposta_6=F('num_pergunta_12_resposta_6')+1)
		elif(Dados.resposta_pergunta_12 == 7): Contadores.objects.filter(pk=1).update(num_pergunta_12_resposta_7=F('num_pergunta_12_resposta_7')+1)
		elif(Dados.resposta_pergunta_12 == 8): Contadores.objects.filter(pk=1).update(num_pergunta_12_resposta_8=F('num_pergunta_12_resposta_8')+1)
		elif(Dados.resposta_pergunta_12 == 9): Contadores.objects.filter(pk=1).update(num_pergunta_12_resposta_9=F('num_pergunta_12_resposta_9')+1)
		elif(Dados.resposta_pergunta_12 == 10): Contadores.objects.filter(pk=1).update(num_pergunta_12_resposta_10=F('num_pergunta_12_resposta_10')+1)

			
	def send_email(self, email):
		dados = Dados.objects.last()
		send_mail(
			'[JRS - Consultoria]',
			'Olá, a JRS Consultoria agradece pelo seu contato.',
			settings.DEFAULT_FROM_EMAIL,
			['email'],
			fail_silently=False
		)


class UserAdminForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'name', 'email', 'telefone', 'empresa', 'ramo','is_active', 'is_staff']
