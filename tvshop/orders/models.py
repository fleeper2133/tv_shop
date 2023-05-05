from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import AddressUser, CustomUser
from items.models import Tv


class Order(models.Model):
    customer_user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    customer_first_name = models.CharField('Имя покупателя', max_length=150)
    customer_last_name = models.CharField('Фамилия покупателя', max_length=150)
    customer_email = models.EmailField('Email покупателя')
    customer_phone = PhoneNumberField('Номер телефона покупателя')
    customer_address = models.OneToOneField(AddressUser, on_delete=models.PROTECT)
    tv = models.ManyToManyField(Tv, through='OrderTV', verbose_name='Телевизоры')
    note = models.TextField('Пометки', blank=True)
    time_create = models.DateTimeField('Дата и время создание', auto_now_add=True)

    def __str__(self):
        return self.customer_email

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"


class OrderTV(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name="Заказ")
    tv = models.ForeignKey(Tv, on_delete=models.PROTECT, verbose_name="Телевизор")
    quantity = models.IntegerField('Кол-во', default=1)

    class Meta:
        verbose_name = 'Заказ-Телевизор'
        verbose_name_plural = "Заказы-Телевизоры"

