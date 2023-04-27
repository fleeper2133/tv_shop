from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from .forms import LoginForm, CustomUserCreationForm
from .models import CustomUser
from .forms import CustomUserChangeForm, AddressUserChangeForm


def user_logout(request):
    logout(request)
    return redirect('login')


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('home')


class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/reg.html'
    extra_context = {"title": "Регистрация"}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class UserProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(pk=self.request.user.pk)
        context['user'] = user
        context['title'] = "Профиль"
        return context


class UserProfileUpdateView(View):
    template_name = 'users/profile_update.html'

    def get(self, request):
        user_form = CustomUserChangeForm(instance=request.user)

        return render(request, self.template_name, {"user_form": user_form})






