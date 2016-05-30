from django.http import Http404
from django.shortcuts import render
from .models import  Album

def index(request):   # request here is an HTTP request
    all_albums = Album.objects.all()    #all_albums is a var to store all albums
    context = {'all_albums' : all_albums}  #context is just a user defined name for a dictionary
    return render(request, 'music/index.html', context)

def detail(request, album_id):
      try:
          album  = Album.objects.get(pk=album_id)
      except Album.DoesNotExist:
          raise Http404("Album does not exist")
      return render(request, 'music/detail.html', {'album' : album})