from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("Email", unique=True)
    phone = PhoneNumberField(_("phone"), default=None, null=True, unique=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class AddressUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    street = models.CharField('Адрес', max_length=255, blank=True)
    corpus = models.IntegerField("Корпус", blank=True, null=True)
    house = models.IntegerField('Дом', blank=True, null=True)
    flat = models.IntegerField("Квартира", blank=True, null=True)
    postcode = models.CharField('Почтовый индекс', max_length=30, blank=True)
    city = models.CharField('Город', max_length=50, blank=True)
    country = models.CharField("Страна", max_length=50, blank=True)

    def __str__(self):
        if self.house:
            return str(self.street) + " " + str(self.house)
        return self.street

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"


@receiver(post_save, sender=CustomUser)
def create_address_user(sender, instance, created, **kwargs):
    if created:
        AddressUser.objects.create(user=instance)
