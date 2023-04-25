from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import LoginForm, CustomUserCreationForm


def user_logout(request):
    logout(request)
    return redirect('login')


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}

    def get_success_url(self):
        return redirect('home')


class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/reg.html'
    extra_context = {"title": "Регистрация"}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



