# Generated by Django 5.1.4 on 2024-12-30 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_floor_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='clean_date',
            field=models.DateField(auto_now=True, verbose_name='Дата уборки'),
        ),
        migrations.AlterField(
            model_name='floor',
            name='fix_date',
            field=models.DateField(auto_now=True, verbose_name='Дата ремонта'),
        ),
        migrations.AlterField(
            model_name='floor',
            name='rooms_count',
            field=models.IntegerField(default=0, verbose_name='Количество номеров'),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.floor', verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='room',
            name='guest_count',
            field=models.IntegerField(default=2, verbose_name='Количество гостей'),
        ),
        migrations.AlterField(
            model_name='room',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Готовность номера'),
        ),
        migrations.AlterField(
            model_name='room',
            name='is_occupied',
            field=models.BooleanField(default=False, verbose_name='Занятость номера'),
        ),
        migrations.AlterField(
            model_name='room',
            name='phone',
            field=models.IntegerField(default=0, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.roomtype', verbose_name='Категория номера'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='guest_count',
            field=models.IntegerField(default=2, verbose_name='Количество спальных мест'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='night_cost',
            field=models.IntegerField(default=0, verbose_name='Стоимость за ночь'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='room_category',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Категория номера'),
        ),
    ]
