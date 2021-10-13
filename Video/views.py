from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Vid
from .forms import Vid_Form
from django.contrib.auth.decorators import login_required



@login_required
def play_vid(request):
    last_vid = Vid.objects.last()
    vid_file = last_vid.vid_file if last_vid else None

    form = Vid_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        data = form.cleaned_data
        Vid.objects.create(username=request.user, vid_file=data['vid_file'])

        return HttpResponseRedirect(reverse('home'))
    form = Vid_Form()

    
    clip= {'vid_file': vid_file,
              'form': form
              }
    
    
    return render(request, 'video.html', clip)

    

