from django.conf.urls import url, include
from . import views

app_name = 'casts'

urlpatterns = [
    url(r'^$', views.index)
]
