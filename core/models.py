from django.db import models
from django.contrib.auth.models import AbstractUser
import psycopg2

class User(AbstractUser):
    pass

class Habit(model.Models):

    habit = models.CharField(max_length=150)
    