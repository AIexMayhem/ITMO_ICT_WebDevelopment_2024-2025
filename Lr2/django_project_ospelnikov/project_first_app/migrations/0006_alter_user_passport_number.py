# Generated by Django 5.1.2 on 2024-11-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0005_car_owner_user_owner_passport_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passport_number',
            field=models.CharField(max_length=10),
        ),
    ]
