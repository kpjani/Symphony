from django.http import HttpResponse
from django.shortcuts import render
from .models import  Album

def index(request):   # request here is an HTTP request
    all_albums = Album.objects.all()    #all_albums is a var to store all albums
    context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")