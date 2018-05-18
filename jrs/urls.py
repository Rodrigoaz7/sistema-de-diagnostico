"""jrs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeView, get_data
from sitio.views import ChartData
from django.contrib.auth.views import login, logout
from home import views as homeviews
from sitio import views


urlpatterns = [
    url(r'^$', ChartData.question, name='index'),
    url(r'^relatorio/$', HomeView.as_view(), name='home'),
    url(r'^diagnostico/', include('diagnostico.urls', namespace='diagnostico')),
	url(r'^pdf', views.generatePDF, name = 'pdf'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^api/chart/data/admin$', ChartData.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^login2', homeviews.login_view, name = 'login'),
    url(r'^logout', homeviews.logout_view, name = 'logout'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^login/', include('accounts.urls', namespace='accounts')),
    url(r'^sair/$', logout, {'next_page': 'relatorio.html'}, name='sair'),
]

