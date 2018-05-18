from .models import Control

def delete_users(self):	
		Control.objects.all().delete()