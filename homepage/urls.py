from django.conf.urls import url

from . import views

app_name = 'homepage'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'logout/$', views.logout_view, name='logout'),

]