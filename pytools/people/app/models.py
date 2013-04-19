from django.db import models

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=1024)
    gender = models.CharField(max_length=10)
    profession = models.CharField(max_length=1024)
    country = models.CharField(max_length=1024)


class Names(models.Model):
    name = models.CharField(max_length=1024)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=1024)
    city = models.CharField(max_length=1024)
    crawled = models.BooleanField(default=False)
    success = models.BooleanField(default=False)
