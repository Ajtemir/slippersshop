from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

class Product(models.Model):
    SABO = 'sabo'
    SLIPPERS = 'slippers'
    HOMESLIPS = 'homeslips'
    SANDALS = 'sandals'
    CHOICE_GROUP = {
        (SABO, 'Сабо'),
        (SLIPPERS, 'Шлёпанцы'),
        (HOMESLIPS, 'Домашки'),
        (SANDALS, 'Сандалии'),
    }

    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    availability = models.BooleanField(verbose_name='Наличие')
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=SLIPPERS, verbose_name='Категории')
    img = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    uploaded = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = ('id',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:detail', args=[self.id])
