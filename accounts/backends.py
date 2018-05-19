from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from django.contrib.auth import get_user_model
from .models import User

class ModelBackend(BaseModelBackend):
	#Função de autenticação de login por email apenas
	def authenticate(self, email=None):
		if not email is None:
			try:
				user = User.objects.get(email=email)
				return user
			except User.DoesNotExist:
				pass
