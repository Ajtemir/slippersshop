# Generated by Django 3.2.5 on 2021-07-29 20:18

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('availability', models.BooleanField(verbose_name='Наличие')),
                ('group', models.CharField(choices=[('sandals', 'Сандалии'), ('homeslips', 'Домашки'), ('sabo', 'Сабо'), ('slippers', 'Шлёпанцы')], default='slippers', max_length=20, verbose_name='Категории')),
                ('img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('uploaded', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
                'index_together': {('id',)},
            },
        ),
    ]
