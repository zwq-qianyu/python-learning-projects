from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^fun/([0-9]{4})/([a-z]+)$', views.fun),
    url(r'^fun2$', views.fun2),
]