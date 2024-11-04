from django.db import models
from django.contrib.auth.models import AbstractUser

from django_project_ospelnikov import settings


class User(AbstractUser):
    passport = models.CharField(max_length=10, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Car(models.Model):
    car_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    owner = models.ManyToManyField(Owner, through='Own')

class Own(models.Model):
    car_owner_id = models.ForeignKey(Owner,on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)


class DrivingLicence(models.Model):
    car_owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    licence_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateField()


