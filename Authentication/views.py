from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from Authentication.forms import LoginForm, SignUpForm
from Account.models import MyUser
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
# Login, Signup, and Logout views

class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('password1') == data.get('password2'):
                try:
                    check = MyUser.objects.get(username=data.get('username'))
                    context = {'form': form}
                    print('Username is already taken!')
                    messages.error(request, 'Username already taken!')
                    return render(request, 'username_taken.html', context)
                except MyUser.DoesNotExist:
                    user = MyUser.objects.create_user(
                        username=data.get('username'),
                        password=data.get('password1'),
                        email=data.get('email'),
                        age=data.get('age'),
                        bio=data.get('bio'),
                        )
                    login(request, user)
                    return redirect(reverse('homepage'))
            else:
                context = {'form': form}
                print('Passwords do not match!')
                messages.error(request, 'Passwords do not match!')
                return render(request, 'pwmatch.html', context)
        else:
            form = SignUpForm()
            return render(request, 'signup.html', {'form': form})



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data.get('username'),
                password=data.get('password')
            )
            if user:
                login(request, user)
                return redirect(request.GET.get('next', 'homepage'))
            else:
                return render(request, 'incorrect.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('homepage'))


