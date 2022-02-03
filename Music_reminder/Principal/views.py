from django.shortcuts import render
from datetime import datetime
def home(request):
    
    # current date and time
    now = datetime.now()

    timestamp = datetime.timestamp(now)

    return render(request,"home.html",{"song_timestamp":timestamp})
  