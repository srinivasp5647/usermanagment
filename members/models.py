from django.db import models
from rest_framework.fields import CharField


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    usernameasemail = models.BooleanField()
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.name