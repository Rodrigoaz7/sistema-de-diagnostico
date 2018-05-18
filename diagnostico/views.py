
from django.shortcuts import render,redirect
from sitio.models import Control
from django.conf import settings
from django.views import generic
from django.views.generic import View, TemplateView
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import get_messages



class RelatorioView(LoginRequiredMixin,TemplateView):
        usuarios = User.objects.all().count()
        template_name = 'diagnostico/relatorio.html'


index = RelatorioView.as_view()

def index(request):
    usuarios = User.objects.all().count()
    context = {
        'cont_usuarios': cont_usuarios,
    }
    return render (request, 'diagnostico/relatorio.html', context)
