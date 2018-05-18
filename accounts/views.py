from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, TemplateView, UpdateView, FormView, ListView
from django.contrib.auth.forms import PasswordChangeForm
from django.core.urlresolvers import reverse_lazy
from .models import User
from .forms import UserAdminCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

#Pôr o LoginRequiredMixin como parâmetro da classe, obriga o usuário a estar logado
#class IndexView(TemplateView):
#	template_name = 'accounts/templates/register.html'


#class RegisterView(CreateView, FormView):
#	model = User
#	template_name = 'accounts/templates/register.html'
#	set_unusable_password()
#	form_class = UserAdminCreationForm
#	success_url = reverse_lazy('accounts:index')

#index = IndexView.as_view()
#register = RegisterView.as_view()
#update_user = UpdateUserView.as_view()
#update_password = UpdatePasswordView.as_view()
