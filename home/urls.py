from home import views
from django.conf.urls import url

urlpatterns = [
	url(r'^login', views.login_view, name = 'login'),
    url(r'^logout', views.logout_view, name = 'logout'),
]