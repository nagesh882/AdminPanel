from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=55)
    userSurname = models.CharField(max_length=55)
    userPhone = models.IntegerField()
    userEmail = models.EmailField(max_length=150)
    userAddress = models.TextField()

# Create your models here.