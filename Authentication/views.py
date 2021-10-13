from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from Authentication.forms import LoginForm, SignUpForm
from Account.models import MyUser
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
            if data.password1 == data.password2:
                try:
                    user = MyUser.objetcs.get(username=data.username)
                    context = {'form':form, 'error': 'This username already exists'}
                    return render(request, 'signup.html', context)
                except MyUser.DoesNotExist:
                    user = MyUser.objects.create_user(
                        username=data.get('username'),
                        password=data.get('password1'),
                        email=data.get('email'),
                        age=data.get('age'),
                        bio=data.get('bio')
                    )
                    login(request, user)
                    return redirect(reverse('homepage'))
            else:
                context = {'form': form, 'error': 'The passwords do not match'}
                return render(request, 'signup.html', context)
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


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('homepage'))


#temporary for testing
@login_required
def index_view(request):
    form = SignUpForm()
    return render(request, 'index.html', {'form': form})
