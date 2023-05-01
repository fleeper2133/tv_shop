# Generated by Django 4.2 on 2023-04-26 21:54

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255, verbose_name='Адрес')),
                ('corpus', models.IntegerField(blank=True, null=True, verbose_name='Корпус')),
                ('house', models.IntegerField(blank=True, null=True, verbose_name='Дом')),
                ('flat', models.IntegerField(blank=True, null=True, verbose_name='Квартира')),
                ('postcode', models.CharField(max_length=30, verbose_name='Почтовый индекс')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None, unique=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.addressuser'),
        ),
    ]
