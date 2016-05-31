from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import  Album, Song


def index(request):   # request here is an HTTP request
    all_albums = Album.objects.all()    #all_albums is a var to store all albums
    context = {'all_albums' : all_albums}  #context is just a user defined name for a dictionary
    return render(request, 'music/index.html', context)

def detail(request, album_id):
      #try:
          #album  = Album.objects.get(pk=album_id)
      #except Album.DoesNotExist:
          #raise Http404("Album does not exist")
      #the below 1 line replaces this try except block
      album = get_object_or_404(Album, pk=album_id)
      return render(request, 'music/detail.html', {'album' : album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album' : album,
            'error_message' : "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})