from django.db import models
import re
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.models import User

# ************ ATENÇÃO - SE FOR USAR ISSO, FAÇA DESDE O INÍCIO !!! ***********************
# ********   APP ACCOUNTS PARA CONSTRUÇÃO DE USUÁRIOS CUSTOMIZADO !! *****************************
class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(
		'Apelido / Usuário', max_length=30, unique=True, validators=[
			validators.RegexValidator(
				re.compile('^[\w.@+-]+$'),
				'Informe um nome de usuário válido. '
				'Este valor deve conter apenas letras, números '
				'e os caracteres: @/./+/-/_ .'
				, 'invalid'
			)
		], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
	)
	#Como o sistema não necessita de login, então não é necessário haver campos únicos
	User._meta.get_field('username')._unique = False
	
	name = models.CharField('Nome', max_length=100, blank=True, unique=False)
	email = models.EmailField('E-mail', unique=True)
	telefone = models.CharField('Telefone', max_length=17,unique=False)
	empresa = models.CharField('Empresa', max_length=100,unique=False)
	ramo = models.CharField('Ramo', max_length=100,unique=False)
	is_staff = models.BooleanField('Equipe', default=False) #boolean
	is_active = models.BooleanField('Ativo', default=True) #boolean
	#date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email'] #Campo requerido na criação de super Usuários

	objects = UserManager()

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

	def __str__(self):
		return self.name or self.username

	def get_full_name(self):
		return str(self)

	def get_short_name(self):
		return str(self).split(" ")[0]
