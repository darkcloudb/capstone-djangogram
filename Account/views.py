from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from Account.forms import EditBioForm
from Account.models import MyUser
from Photo.models import PostImg
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
# Create your views here.

class LoggedInView(LoginRequiredMixin, View):
    def get(self, request):
        posts = PostImg.objects.all().order_by('-posted_at')
        return render(request, 'homepage.html', {'posts': posts})


def profile_detail(request, id):
    template_name = "profile.html"
    profile = MyUser.objects.get(id=id)
    context = {"profile": profile}
    return render(request, template_name, context)


@login_required
def edit(request, id=None, template_name='profile.html'):
    if id:
        bio = get_object_or_404(MyUser, pk=id)
        if bio.username != request.user:
            return HttpResponseForbidden()
    else:
        bio = MyUser(username=request.user)
        form = EditBioForm(request.POST or None, instance=bio)
        if request.POST and form.is_valid():
            form.save()
            redirect_url = reverse('bio_save_success')
            return redirect(redirect_url)
    return render(request, template_name, {
        'form': form
    })
