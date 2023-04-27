from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from .forms import LoginForm, CustomUserCreationForm
from .models import CustomUser, AddressUser
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
        address = AddressUser.objects.get(user_id=self.request.user.pk)
        context['user'] = user
        context['address'] = address
        context['title'] = "Профиль"
        return context


class UserProfileUpdateView(View):
    template_name = 'users/profile_update.html'

    def get(self, request):
        user_form = CustomUserChangeForm(instance=request.user)
        address = AddressUser.objects.get(user=request.user)
        address_form = AddressUserChangeForm(instance=address)

        data = {
            "user_form": user_form,
            "address_form": address_form,
            "title": "Настройки профиля"
        }

        return render(request, self.template_name, data)

    def post(self, request):
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        address = AddressUser.objects.get(user=request.user)
        address_form = AddressUserChangeForm(request.POST, instance=address)

        if user_form.is_valid() and address_form.is_valid():
            user_form.save()
            address_form.save()

            return redirect('profile')

        data = {
            "user_form": user_form,
            "address_form": address_form,
            "title": "Настройки профиля"
        }

        return render(request, self.template_name, data)






