from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from Photo.models import PostImg

# Create your views here.

class LoggedInView(LoginRequiredMixin, View):
    def get(self, request):
        posts = PostImg.objects.all().order_by('-posted_at')
        return render(request, 'homepage.html', {'posts': posts})
