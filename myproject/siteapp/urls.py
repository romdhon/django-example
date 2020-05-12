from django.conf.urls import url 
from . import views

app_name = 'siteapp'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.user_login, name='user_login')
]