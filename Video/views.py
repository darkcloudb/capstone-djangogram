from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import Vid
from .forms import Vid_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View



@login_required
def play_vid(request):
    last_vid = Vid.objects.last()
    vid_file = last_vid.vid_file if last_vid else None
    form = Vid_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        data = form.cleaned_data
        Vid.objects.create(username=request.user, vid_file=data['vid_file'])

        return HttpResponseRedirect(reverse('video'))
    form = Vid_Form()
    clip = {'vid_file': vid_file,
            'form': form
            }
    return render(request, 'video.html', clip)


class VidDelete(LoginRequiredMixin, View):
    def get(self, request, post_id=None):
        post = Vid.objects.get(id=post_id)
        if request.user.is_staff or request.user == post.username:
            post.delete()
            return redirect(reverse('homepage'))
        else:
            # return HttpResponse("Access Denied - Only Original Poster or Admin can delete this image.")
            return render(request, '403.html')
