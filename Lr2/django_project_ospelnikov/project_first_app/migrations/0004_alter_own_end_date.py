# Generated by Django 5.1.2 on 2024-11-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_alter_own_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='own',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
