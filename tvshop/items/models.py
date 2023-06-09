from django.db import models
from django.urls import reverse


class Tv(models.Model):
    title = models.CharField("Название", max_length=255)
    type_tv = models.CharField("Тип", max_length=255)
    model = models.ForeignKey('Model', null=True, on_delete=models.SET_NULL, verbose_name="Модель")
    content = models.TextField("Описание")
    value = models.IntegerField("Цена")
    discount_value = models.IntegerField("Цена со скидкой", null=True, blank=True)
    diagonal = models.FloatField("Диагональ")
    resolution = models.CharField("Разрешение", max_length=50)
    frequency = models.IntegerField("Частота")
    sound_power = models.IntegerField("Мощность звука")
    wi_fi = models.BooleanField("wi-fi")
    smart_tv = models.BooleanField()
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField("Публикация", default=True)
    photo = models.ImageField("Фото", upload_to="tvs/%Y/%m/%d/")

    class Meta:
        verbose_name = "Телевизор"
        verbose_name_plural = "Телевизоры"
        ordering = ['-time_create']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk": self.pk})

    def get_value(self):
        if self.discount_value:
            return self.discount_value
        return self.value


class Model(models.Model):
    title = models.CharField("Название", max_length=255)
    slug = models.SlugField("URL")

    class Meta:
        verbose_name = "Модель телевизора"
        verbose_name_plural = "Модели телевизоров"
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('model', kwargs={"model_slug": self.slug})
