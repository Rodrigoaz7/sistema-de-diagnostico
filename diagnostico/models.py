from django.db import models
from django import forms

class Relatorio(models.Model):
	FE = 'Financeiro/Estrutural'
	MK = 'Marketing'
	PP = 'Pessoas/Processos'
	segmentos_choice = (
		(FE, 'Financeiro/Estrutural'),
		(MK, 'Marketing'),
		(PP, 'Pessoas/Processos'),
	)
	#Cada relatorio é feito em relação a um dos três segmentos
	segmentos = models.CharField(max_length=50, choices=segmentos_choice, default=FE)
	#Cada segmento possui 3 niveis (3 relatorios diferentes)
	nivel = models.IntegerField('Nivel (1, 2 ou 3)')
	titulo = models.CharField(max_length=200)
	texto = models.TextField(blank=True)	

	class Meta:
		verbose_name = 'Relatório'
		verbose_name_plural = 'Relatórios'
		ordering = ['nivel'] 