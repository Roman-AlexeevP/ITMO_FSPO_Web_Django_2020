
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

class People(AbstractUser):
    address = models.CharField(max_length=512, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    passport = models.CharField(max_length=10, blank=True, null=True)

class Car(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    number = models.CharField(max_length=9)



class User(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    people = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    passport = models.IntegerField
    gender = models.CharField(max_length=3, choices=GENDER)

    users = models.ManyToManyField(Car, through='Ownership')


class Ownership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()


class License(models.Model):
    TYPE = (
        ('A', 'A'),
        ('A1', 'A1'),
        ('B', 'B'),
        ('B1', 'B1'),
        ('C', 'C'),
        ('C1', 'C1'),
        ('D', 'D'),
        ('D1', 'D1')
    )
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.IntegerField
    type = models.CharField(max_length=3, choices=TYPE)
    date_issued = models.DateField()
