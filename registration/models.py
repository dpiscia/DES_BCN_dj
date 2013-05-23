from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=40)
    Surnname = models.CharField(max_length=40)
    email = models.CharField(max_length=40)