# Generated by Django 5.1.4 on 2024-12-30 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_guest_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Бронь', 'verbose_name_plural': 'Брони'},
        ),
    ]
