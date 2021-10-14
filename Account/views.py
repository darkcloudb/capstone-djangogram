from typing import AsyncGenerator, BinaryIO
from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404, redirect
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
 

class EditProfile(LoginRequiredMixin, View):
    def get(self, request, id):
        profile = MyUser.objects.get(id=id)
        if request.user.id == id:
            form = EditBioForm(initial={
                'bio': profile.bio,
                'age': profile.age,
                'email': profile.email,
            })
            return render(request, 'generic_form.html', {'form': form})
        else:
            return render(request, '403.html')

    def post(self, request, id):
        profile = MyUser.objects.get(id=id)
        form = EditBioForm(request.POST, request.FILES)
        print(profile)
        if form.is_valid():
            data = form.cleaned_data
            profile.bio = data['bio']
            profile.age = data['age']
            profile.email = data['email']
            profile.prof_pic = data['prof_pic']
            profile.save()
            return HttpResponseRedirect(reverse('profile', args=(id,)))
        return HttpResponseRedirect(reverse('profile', args=(id,)))
