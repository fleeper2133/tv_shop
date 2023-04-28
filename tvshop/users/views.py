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
        return reverse_lazy('profile')


class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/reg.html'
    extra_context = {"title": "Регистрация"}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


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


def user_profile_update(request):
    template_name = 'users/profile_update.html'

    address = AddressUser.objects.get(user=request.user)

    if request.POST:
        request_update = request.POST.copy()
        if request_update.get('phone') == '+7':
            request_update.update({'phone': ''})

        user_form = CustomUserChangeForm(request_update, instance=request.user)
        address_form = AddressUserChangeForm(request_update, instance=address)

        if user_form.is_valid() and address_form.is_valid():
            user_form.save()
            address_form.save()

            return redirect('profile')

    user_form = CustomUserChangeForm(instance=request.user)
    address_form = AddressUserChangeForm(instance=address)

    data = {
        "user_form": user_form,
        "address_form": address_form,
        "title": "Настройки профиля"
    }

    return render(request, template_name, data)






