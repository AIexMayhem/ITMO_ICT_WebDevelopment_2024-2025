# Generated by Django 5.1.2 on 2024-11-04 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_desc', '0002_rename_marks_mark_rename_readytasks_readytask_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_desc.user'),
        ),
    ]
