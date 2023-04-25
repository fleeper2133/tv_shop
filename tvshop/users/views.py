from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .forms import LoginForm


def test(request):
    return render(request, 'users/login.html')


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}
