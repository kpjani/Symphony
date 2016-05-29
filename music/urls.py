from django.conf.urls import url
from . import views  # . is current directory

urlpatterns = [
    url(r'^$', views.index, name='index'),  #look for function named 'index' in views.py
]