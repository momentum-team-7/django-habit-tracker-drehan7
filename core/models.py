from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class HabitLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    track_unit = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} | {self.track_unit}"

class Habit(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(max_length=250, blank=True, null=True)
    log = models.ForeignKey(HabitLog, on_delete=models.CASCADE, null=True, blank=True)
    goal = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} {self.description} {self.goal}"


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"