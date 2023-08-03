from django.db import models

from django.db import models


class Bird(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название птицы')
    color = models.CharField(max_length=50, verbose_name='Цвет перьев')
    photo = models.ImageField(upload_to='bird_photos/', verbose_name='Фотография')
    sightings = models.PositiveIntegerField(default=0, verbose_name='Количество наблюдений')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Птица'
        verbose_name_plural = 'Птицы'
