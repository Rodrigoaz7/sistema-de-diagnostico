from django.db import models

class Question(models.Model):
	FE = 'Financeiro/Estrutural'
	MK = 'Marketing'
	PP = 'Pessoas/Processos'
	segmentos_choice = (
		(FE, 'Financeiro/Estrutural'),
		(MK, 'Marketing'),
		(PP, 'Pessoas/Processos'),
	)
	segmentos = models.CharField(max_length=50, choices=segmentos_choice, default=FE)
	text = models.TextField('Questão', blank=False)

	#Pegar a data em que o modelo é criado !!
	created = models.DateTimeField('Criado em', auto_now_add=True)
	#Pegar a data em que o modelo é salvo (ultima modificacao)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	class Meta:
		verbose_name = 'Questão'
		verbose_name_plural = 'Questões'
		ordering = ['segmentos'] 

class Control(models.Model):
	identificador = models.EmailField('E-mail adicionado', null=False)
	created = models.DateTimeField('Adicionado em', auto_now_add=True)

	class Meta:
		verbose_name = 'Controle'
		verbose_name_plural = 'Controles'
		ordering = ['identificador']        

class Description(models.Model):
    message_form = models.TextField('Descrição para o Formulário', blank=True)
    message_register = models.TextField('Descrição para o Cadastro', blank=True)

    class Meta:
        verbose_name = 'Descrição'
        verbose_name_plural = 'Descrições'
        ordering = ['message_form']        


class Dados(models.Model):
	id_usuario = models.IntegerField('ID do usuário enviado', default=0)
	email_usuario = models.EmailField('E-mail do usuário enviado', default='email@email.com')
	media_Financeiro_Estrutural = models.FloatField('Média do envio das perguntas sobre Financeiro/Estrutural', default=0)
	media_Marketing = models.FloatField('Média do envio das perguntas sobre Marketing', default=0)
	media_Pessoas_Processos = models.FloatField('Média do envio das perguntas sobre Pessoas/Processos', default=0)
	nivel_Financeiro_Estrutural = models.IntegerField('Nível do envio das perguntas sobre Financeiro/Estrutural', default=0)
	nivel_Marketing = models.IntegerField('Nível do envio das perguntas sobre Marketing', default=0)
	nivel_Pessoas_Processos = models.IntegerField('Nível do envio das perguntas sobre Pessoas/Processos', default=0)
	resposta_pergunta_1 = models.IntegerField('Resposta para a pergunta de id 1', default=1)
	resposta_pergunta_2 = models.IntegerField('Resposta para a pergunta de id 2', default=1)
	resposta_pergunta_3 = models.IntegerField('Resposta para a pergunta de id 3', default=1)
	resposta_pergunta_4 = models.IntegerField('Resposta para a pergunta de id 4', default=1)
	resposta_pergunta_5 = models.IntegerField('Resposta para a pergunta de id 5', default=1)
	resposta_pergunta_6 = models.IntegerField('Resposta para a pergunta de id 6', default=1)
	resposta_pergunta_7 = models.IntegerField('Resposta para a pergunta de id 7', default=1)
	resposta_pergunta_8 = models.IntegerField('Resposta para a pergunta de id 8', default=1)
	resposta_pergunta_9 = models.IntegerField('Resposta para a pergunta de id 9', default=1)
	resposta_pergunta_10 = models.IntegerField('Resposta para a pergunta de id 10', default=1)
	resposta_pergunta_11 = models.IntegerField('Resposta para a pergunta de id 11', default=1)
	resposta_pergunta_12 = models.IntegerField('Resposta para a pergunta de id 12', default=1)
	
	
	class Meta:
		verbose_name = 'Dado'
		verbose_name_plural = 'Dados'
		ordering = ['nivel_Financeiro_Estrutural']

class Contadores(models.Model):
	num_financeiro_estrutural_nivel_1 = models.SmallIntegerField('Contador financeiro p/ nivel 1', default=0)
	num_financeiro_estrutural_nivel_2 = models.SmallIntegerField('Contador financeiro p/ nivel 2', default=0)
	num_financeiro_estrutural_nivel_3 = models.SmallIntegerField('Contador financeiro p/ nivel 3', default=0)
	num_marketing_nivel_1 = models.SmallIntegerField('Contador marketing p/ nivel 1', default=0)
	num_marketing_nivel_2 = models.SmallIntegerField('Contador marketing p/ nivel 2', default=0)
	num_marketing_nivel_3 = models.SmallIntegerField('Contador marketing p/ nivel 3', default=0)
	num_pessoas_processos_nivel_1 = models.SmallIntegerField('Contador pessoas p/ nivel 1', default=0)
	num_pessoas_processos_nivel_2 = models.SmallIntegerField('Contador pessoas p/ nivel 2', default=0)
	num_pessoas_processos_nivel_3 = models.SmallIntegerField('Contador pessoas p/ nivel 3', default=0)
	
	num_pergunta_1_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 1', default=0)
	num_pergunta_1_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 1', default=0)
	num_pergunta_1_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 1', default=0)
	num_pergunta_1_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 1', default=0)
	num_pergunta_1_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 1', default=0)
	num_pergunta_1_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 1', default=0)
	num_pergunta_1_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 1', default=0)
	num_pergunta_1_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 1', default=0)
	num_pergunta_1_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 1', default=0)
	num_pergunta_1_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 1', default=0)
	
	num_pergunta_2_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 2', default=0)
	num_pergunta_2_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 2', default=0)
	num_pergunta_2_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 2', default=0)
	num_pergunta_2_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 2', default=0)
	num_pergunta_2_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 2', default=0)
	num_pergunta_2_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 2', default=0)
	num_pergunta_2_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 2', default=0)
	num_pergunta_2_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 2', default=0)
	num_pergunta_2_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 2', default=0)
	num_pergunta_2_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 2', default=0)
	
	num_pergunta_3_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 3', default=0)
	num_pergunta_3_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 3', default=0)
	num_pergunta_3_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 3', default=0)
	num_pergunta_3_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 3', default=0)
	num_pergunta_3_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 3', default=0)
	num_pergunta_3_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 3', default=0)
	num_pergunta_3_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 3', default=0)
	num_pergunta_3_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 3', default=0)
	num_pergunta_3_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 3', default=0)
	num_pergunta_3_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 3', default=0)
	
	num_pergunta_4_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 4', default=0)
	num_pergunta_4_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 4', default=0)
	num_pergunta_4_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 4', default=0)
	num_pergunta_4_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 4', default=0)
	num_pergunta_4_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 4', default=0)
	num_pergunta_4_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 4', default=0)
	num_pergunta_4_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 4', default=0)
	num_pergunta_4_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 4', default=0)
	num_pergunta_4_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 4', default=0)
	num_pergunta_4_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 4', default=0)
	
	num_pergunta_5_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 5', default=0)
	num_pergunta_5_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 5', default=0)
	num_pergunta_5_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 5', default=0)
	num_pergunta_5_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 5', default=0)
	num_pergunta_5_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 5', default=0)
	num_pergunta_5_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 5', default=0)
	num_pergunta_5_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 5', default=0)
	num_pergunta_5_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 5', default=0)
	num_pergunta_5_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 5', default=0)
	num_pergunta_5_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 5', default=0)
	
	num_pergunta_6_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 6', default=0)
	num_pergunta_6_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 6', default=0)
	num_pergunta_6_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 6', default=0)
	num_pergunta_6_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 6', default=0)
	num_pergunta_6_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 6', default=0)
	num_pergunta_6_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 6', default=0)
	num_pergunta_6_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 6', default=0)
	num_pergunta_6_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 6', default=0)
	num_pergunta_6_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 6', default=0)
	num_pergunta_6_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 6', default=0)
	
	num_pergunta_7_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 7', default=0)
	num_pergunta_7_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 7', default=0)
	num_pergunta_7_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 7', default=0)
	num_pergunta_7_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 7', default=0)
	num_pergunta_7_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 7', default=0)
	num_pergunta_7_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 7', default=0)
	num_pergunta_7_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 7', default=0)
	num_pergunta_7_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 7', default=0)
	num_pergunta_7_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 7', default=0)
	num_pergunta_7_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 7', default=0)
	
	num_pergunta_8_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 8', default=0)
	num_pergunta_8_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 8', default=0)
	num_pergunta_8_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 8', default=0)
	num_pergunta_8_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 8', default=0)
	num_pergunta_8_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 8', default=0)
	num_pergunta_8_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 8', default=0)
	num_pergunta_8_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 8', default=0)
	num_pergunta_8_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 8', default=0)
	num_pergunta_8_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 8', default=0)
	num_pergunta_8_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 8', default=0)
	
	num_pergunta_9_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 9', default=0)
	num_pergunta_9_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 9', default=0)
	num_pergunta_9_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 9', default=0)
	num_pergunta_9_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 9', default=0)
	num_pergunta_9_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 9', default=0)
	num_pergunta_9_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 9', default=0)
	num_pergunta_9_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 9', default=0)
	num_pergunta_9_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 9', default=0)
	num_pergunta_9_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 9', default=0)
	num_pergunta_9_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 9', default=0)
	
	num_pergunta_10_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 10', default=0)
	num_pergunta_10_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 10', default=0)
	num_pergunta_10_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 10', default=0)
	num_pergunta_10_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 10', default=0)
	num_pergunta_10_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 10', default=0)
	num_pergunta_10_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 10', default=0)
	num_pergunta_10_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 10', default=0)
	num_pergunta_10_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 10', default=0)
	num_pergunta_10_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 10', default=0)
	num_pergunta_10_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 10', default=0)

	num_pergunta_11_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 11', default=0)
	num_pergunta_11_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 11', default=0)
	num_pergunta_11_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 11', default=0)
	num_pergunta_11_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 11', default=0)
	num_pergunta_11_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 11', default=0)
	num_pergunta_11_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 11', default=0)
	num_pergunta_11_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 11', default=0)
	num_pergunta_11_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 11', default=0)
	num_pergunta_11_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 11', default=0)
	num_pergunta_11_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 11', default=0)
	
	num_pergunta_12_resposta_1 = models.SmallIntegerField('Contador resposta 1 p/ pergunta 12', default=0)
	num_pergunta_12_resposta_2 = models.SmallIntegerField('Contador resposta 2 p/ pergunta 12', default=0)
	num_pergunta_12_resposta_3 = models.SmallIntegerField('Contador resposta 3 p/ pergunta 12', default=0)
	num_pergunta_12_resposta_4 = models.SmallIntegerField('Contador resposta 4 p/ pergunta 12', default=0)
	num_pergunta_12_resposta_5 = models.SmallIntegerField('Contador resposta 5 p/ pergunta 12', default=0)
	num_pergunta_12_resposta_6 = models.SmallIntegerField('Contador resposta 6 p/ pergunta 12', default=0)
	num_pergunta_12_resposta_7 = models.SmallIntegerField('Contador resposta 7 p/ pergunta 12', default=0)
	num_pergunta_12_resposta_8 = models.SmallIntegerField('Contador resposta 8 p/ pergunta 12', default=0)
	num_pergunta_12_resposta_9 = models.SmallIntegerField('Contador resposta 9 p/ pergunta 12', default=0)
	num_pergunta_12_resposta_10 = models.SmallIntegerField('Contador resposta 10 p/ pergunta 12', default=0)
	
	class Meta:
		verbose_name = 'Contador'
		verbose_name_plural = 'Contadores'
		ordering = ['num_financeiro_estrutural_nivel_1']