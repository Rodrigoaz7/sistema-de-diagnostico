from django.conf.urls import url, include
from diagnostico import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]