from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminForm

class UserAdmin(BaseUserAdmin):

	add_form = UserAdminCreationForm	
	add_fieldsets = (
		(None, {
			'fields': ('username', 'name','email','telefone','empresa', 'ramo','password1', 'password2')
		}),
	)

	fieldsets = (
		(None, {
			'fields': ('username', 'email')
		}),
		('Informações básicas', {
			'fields': ('name', 'telefone', 'empresa', 'ramo')
		}),
		(
			'Permissões', {
				'fields': (
					'is_active', 'is_staff','is_superuser', 'groups', 'user_permissions'
				)
			}
		),
	)
	list_display = ['pk', 'username', 'name', 'email', 'telefone', 'empresa', 'ramo']

admin.site.register(User, UserAdmin)