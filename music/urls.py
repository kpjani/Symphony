from django.conf.urls import url
from . import views  # . is current directory

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),  #look for function named 'index' in views.py

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]