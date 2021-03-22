from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils import timezone
import datetime
import psycopg2


class User(AbstractUser):
    pass



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Habit(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    goal = models.IntegerField(default=0)

    def __str__(self):
        return f"Title: {self.title} | desc: {self.description} | Goal: {self.goal}"


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    track_unit = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["date", "habit"], name="unique datelog"),
        ]

    def __str__(self):
        return f"Date: {self.date} | Amount: {self.track_unit}"

