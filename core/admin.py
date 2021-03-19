from django.contrib import admin
from .models import Habit, HabitLog, Profile, User


# Register your models here.

admin.site.register(Habit)
admin.site.register(HabitLog)
admin.site.register(Profile)
admin.site.register(User)