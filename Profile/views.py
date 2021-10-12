from Profile.forms import UserRegisterForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            return HttpResponseRedirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "profile_page.html/", {"form": form})


@login_required
def profile(request):
    return render(request, "profile_page.html/")
