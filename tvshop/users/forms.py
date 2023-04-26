from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "input100", "name": "email"})
    )
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "input100", "name": "pass"})
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "input100",  "name": "pass"})
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def clean_phone(self):
        return self.cleaned_data['phone'] or None


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "input100", "name": "email"})
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "input100",  "name": "pass"}))


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

    def clean_phone(self):
        return self.cleaned_data['phone'] or None
