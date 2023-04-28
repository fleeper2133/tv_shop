from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from .models import CustomUser, AddressUser


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


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "input100", "name": "email"})
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "input100",  "name": "pass"}))


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', "last_name", "phone",)
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Фамилия"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Номер телефона", "value": "+7"})
        }


class AddressUserChangeForm(forms.ModelForm):

    class Meta:
        model = AddressUser
        fields = ('street', 'corpus', 'house', 'flat', 'postcode', 'city', 'country')
        widgets = {
            'street': forms.TextInput(attrs={"class": "form-control", "placeholder": "Улица"}),
            'corpus': forms.TextInput(attrs={"class": "form-control", "placeholder": "Корпус"}),
            'house': forms.TextInput(attrs={"class": "form-control", "placeholder": "Дом"}),
            'flat': forms.TextInput(attrs={"class": "form-control", "placeholder": "Квартира"}),
            'postcode': forms.TextInput(attrs={"class": "form-control", "placeholder": "Почтовый индекс"}),
            'city': forms.TextInput(attrs={"class": "form-control", "placeholder": "Город"}),
            'country': forms.TextInput(attrs={"class": "form-control", "placeholder": "Страна"}),
        }

