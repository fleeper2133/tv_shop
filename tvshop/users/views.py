from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import LoginForm


def user_logout(request):
    logout(request)
    return redirect('login')


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}
