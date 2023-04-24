# Generated by Django 4.2 on 2023-04-24 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Модель телевизора',
                'verbose_name_plural': 'Модели телевизоров',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('type_tv', models.CharField(max_length=255, verbose_name='Тип')),
                ('content', models.TextField(verbose_name='Описание')),
                ('value', models.IntegerField(verbose_name='Цена')),
                ('discount_value', models.IntegerField(blank=True, null=True, verbose_name='Цена со скидкой')),
                ('diagonal', models.FloatField(verbose_name='Диагональ')),
                ('resolution', models.CharField(max_length=50, verbose_name='Разрешение')),
                ('frequency', models.IntegerField(verbose_name='Частота')),
                ('sound_power', models.IntegerField(verbose_name='Мощность звука')),
                ('wi_fi', models.BooleanField(verbose_name='wi-fi')),
                ('smart_tv', models.BooleanField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('photo', models.ImageField(upload_to='tvs/%Y/%m/%d/', verbose_name='Фото')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.model', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Телевизор',
                'verbose_name_plural': 'Телевизоры',
                'ordering': ['-time_create'],
            },
        ),
    ]
