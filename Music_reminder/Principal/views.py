from django.shortcuts import render
import datetime
from .Database import mongo
def home(request):
    
    
    db=mongo()
    songs_info,num_songs=db.querymusic()
    print(songs_info)

    return render(request,"index.html",{"songs":songs_info,"List":range(num_songs)})
    