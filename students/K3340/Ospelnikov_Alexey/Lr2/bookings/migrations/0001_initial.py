# Generated by Django 5.1.4 on 2024-12-24 17:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField(verbose_name='Дата заезда')),
                ('check_out_date', models.DateField(verbose_name='Дата выезда')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активная бронь')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.room', verbose_name='Номер')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Бронирования',
            },
        ),
    ]
