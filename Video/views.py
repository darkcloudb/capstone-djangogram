from django.shortcuts import render
from .models import Vid
from .forms import Vid_Form
from django.contrib.auth.decorators import login_required



@login_required
def play_vid(request):
    last_vid = Vid.objects.last()
    vid_file = last_vid.vid_life

    form = Vid_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    
    clip= {'vid_file': vid_file,
              'form': form
              }
    
    
    return render(request, 'videos.html', clip)

    

