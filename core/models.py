from django.db import models
from django.contrib.auth.models import AbstractUser
import psycopg2

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"