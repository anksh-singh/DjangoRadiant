from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=25)


