from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "input100",
                                                                              "name": "email"}))
    password1 = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput(attrs={"class": "input100",
                                                                                              "name": "pass"}))
    password2 = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput(attrs={"class": "input100",
                                                                                               "name": "pass"}))

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "input100",
                                                            "name": "email"}))
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput(attrs={"class": "input100",
                                                                 "name": "pass"}))


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
