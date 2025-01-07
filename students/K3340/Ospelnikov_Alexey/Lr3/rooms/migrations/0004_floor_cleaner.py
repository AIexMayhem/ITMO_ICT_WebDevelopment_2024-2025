# Generated by Django 5.1.4 on 2024-12-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_alter_floor_clean_date_alter_floor_fix_date_and_more'),
        ('staff', '0005_remove_employee_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='floor',
            name='cleaner',
            field=models.ManyToManyField(related_name='cleaner', to='staff.employee', verbose_name='Уборщик'),
        ),
    ]
