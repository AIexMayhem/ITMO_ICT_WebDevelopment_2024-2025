import datetime

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

def validate_teacher(value):
    if value != "TC":
        raise ValidationError('You have no rights to do this')

class User(models.Model):
    positions = (
        ('ST', 'Student'),
        ('TC', 'Teacher'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=positions)
    email = models.EmailField()
    birth_date = models.DateField()


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class Homework(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    teacher = models.ForeignKey(User,on_delete=models.CASCADE, validators=[validate_teacher])
    issue_date = models.DateField()
    deadline = models.DateField()
    task = models.CharField(max_length=500)
    penalty = models.CharField(max_length=50)


class ReadyTask(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework,on_delete=models.CASCADE)
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    answer = models.CharField(max_length=500)


class Mark(models.Model):
    homework = models.ForeignKey(Homework,on_delete=models.CASCADE)
    mark = models.IntegerField()
    teacher = models.ForeignKey(User,on_delete=models.CASCADE, validators=[validate_teacher])
    comment = models.CharField(max_length=500)


