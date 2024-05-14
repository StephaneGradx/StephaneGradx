from django.db import models

# Create your models here.

class Signup(models.Model):
    nom = models.CharField(max_length=128)
    prenom = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)


