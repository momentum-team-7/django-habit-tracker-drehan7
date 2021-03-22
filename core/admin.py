from django.contrib import admin
from .models import User, Profile, Habit, HabitLog

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Habit)
admin.site.register(HabitLog)