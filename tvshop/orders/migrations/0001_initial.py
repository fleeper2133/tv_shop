# Generated by Django 4.2 on 2023-05-05 19:55

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        ('users', '0004_alter_customuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_first_name', models.CharField(max_length=150, verbose_name='Имя покупателя')),
                ('customer_last_name', models.CharField(max_length=150, verbose_name='Фамилия покупателя')),
                ('customer_email', models.EmailField(max_length=254, verbose_name='Email покупателя')),
                ('customer_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона покупателя')),
                ('note', models.TextField(blank=True, verbose_name='Пометки')),
                ('customer_address', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='users.addressuser')),
            ],
        ),
        migrations.CreateModel(
            name='OrderTV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Кол-во')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.order', verbose_name='Заказ')),
                ('tv', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.tv', verbose_name='Телевизор')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tv',
            field=models.ManyToManyField(through='orders.OrderTV', to='items.tv', verbose_name='Телевизоры'),
        ),
    ]
