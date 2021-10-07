# from django.shortcuts import render, redirect, reverse
# from Comment.forms import CommentForm
# from Comment.models import Comment
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import View

# # Create your views here.
# class PostComment(LoginRequiredMixin, View):
#     def get(self, request, post_id):
#         form = CommentForm()
#         return render(request, 'generic_form.html', {'form': form})

#     def post(self, request, post_id):
#         if request.method == 'POST':
#             form = CommentForm(request.POST, request.FILES)
#             if form.is_valid():
#                 data = form.cleaned_data
#                 post = Comment.objects.create(
#                     body=data['body'],
#                     username=request.user
#                 )
#                 return redirect(reverse("homepage"))
#         return render(request, 'generic_form.html', {'form': form})