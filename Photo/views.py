from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from Photo.models import PostImg
from Comment.models import Comment
from Photo.forms import PostForm
from Comment.forms import CommentForm


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
    # Thank you so much Marcus for the assist in figuring out the issue with our comment 
    def get(self, request, post_id):
        post = PostImg.objects.filter(id=post_id).first()
        form = CommentForm()
        if PostImg.objects.filter(id=post_id).exists():
            return render(request, 'post_detail.html', {'post': post, "form": form})
        else:
            return render(request, '404.html')



    def post(self, request, post_id):
        grab = PostImg.objects.get(id=post_id)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
                make_comment = Comment(
                    username=request.user,
                    body=data['body'],
                    post=grab
                )
                make_comment.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render(request, 'post_detail.html', {'form': form})


class PostDelete(LoginRequiredMixin, View):
    def get(self, request, post_id=None):
        post = PostImg.objects.get(id=post_id)
        if request.user.is_staff or request.user == post.username:
            post.delete()
            return redirect(reverse('homepage'))
        else:
            # return HttpResponse("Access Denied - Only Original Poster or Admin can delete this image.")
            return render(request, '403.html')


class CommentDelete(LoginRequiredMixin, View):
    def get(self, request, post_id=None):
        comment = Comment.objects.get(id=post_id)
        if request.user.is_staff or request.user == comment.username:
            comment.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request, '403.html')


class SuperDelete(LoginRequiredMixin, View):
    def get(self, request, post_id=None):
        comment = Comment.objects.get(id=post_id)
        post = PostImg.objects.get(id=request.user.id)
        if post:
            comment.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return render(request, '403.html')


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
