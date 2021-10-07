from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from Photo.models import PostImg
from Comment.models import Comment
from Photo.forms import PostForm
from Comment.forms import CommentForm
from django.contrib.auth.decorators import login_required


class PostImage(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                post = PostImg.objects.create(
                    image=data['image'],
                    body=data['body'],
                    username=request.user,
                )
                return redirect(reverse("homepage"))
        return render(request, 'generic_form.html', {'form': form})


class PostDetail(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = PostImg.objects.filter(id=post_id).first()
        return render(request, 'post_detail.html', {'post': post})


class PostDelete(LoginRequiredMixin, View):
    def get(self, request, post_id=None):
        post = PostImg.objects.get(id=post_id)
        if request.user.is_staff or request.user == post.username:
            post.delete()
            return redirect(reverse('homepage'))
        else:
            return HttpResponse("Access Denied - Only Original Poster or Admin can delete this image.")

class PostComment(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = PostImg.objects.filter(id=post_id).first()
        form = CommentForm()
        return render(request, 'post_detail.html', {'post': post, 'form': form})

    def post(self, request, post_id):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                make_comment = Comment.objects.create(
                    comment=data['comment'],
                    username=request.user
                )
        else:
            form = CommentForm()
        return render(request, 'post_detail.html', {'post': post, 'form': form})


def like_photo(request, post_id):
    self = request.user
    photo = PostImg.objects.get(id=post_id)
    photo.favorite.add(self)
    photo.likes += 1
    photo.save()
    print(photo.favorite.all())
    return redirect(request.META.get("HTTP_REFERER"))


def unlike_photo(request, post_id):
    self = request.user
    photo = PostImg.objects.get(id=post_id)
    photo.favorite.remove(self)
    photo.dislikes -= 1
    photo.save()
    print(photo.favorite.all())
    return redirect(request.META.get("HTTP_REFERER"))
