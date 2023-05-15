from django import forms
from .models import Order
from users.models import AddressUser


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('customer_first_name', 'customer_last_name', 'customer_email', 'customer_phone', 'note')
        widgets = {
            'customer_first_name': forms.TextInput(attrs={"class": "input", "placeholder": "Имя"}),
            'customer_last_name': forms.TextInput(attrs={"class": "input", "placeholder": "Фамилия"}),
            'customer_email': forms.TextInput(attrs={"class": "input", "placeholder": "Email"}),
            'customer_phone': forms.TextInput(attrs={"class": "input", "placeholder": "Номер телефона"}),
            'note': forms.Textarea(attrs={"class": "input", "placeholder": "Другие пометки"}),

        }


class AddressCustomerForm(forms.ModelForm):

    street = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "input", "placeholder": "Улица"}))
    postcode = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "input",
                                                                            "placeholder": "Почтовый индекс"}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "input", "placeholder": "Город"}))
    country = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "input", "placeholder": "Страна"}))

    class Meta:
        model = AddressUser
        fields = ('street', 'corpus', 'house', 'flat', 'postcode', 'city', 'country')
        widgets = {
            'corpus': forms.TextInput(attrs={"class": "input", "placeholder": "Корпус"}),
            'house': forms.TextInput(attrs={"class": "input", "placeholder": "Дом"}),
            'flat': forms.TextInput(attrs={"class": "input", "placeholder": "Квартира"}),
        }