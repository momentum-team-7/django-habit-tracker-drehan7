from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home_page, name="home_page"),
    path("create_profile/", views.create_profile, name="create_profile"),
    path("add_habit/", views.add_habit, name="add_habit"),
    path("home/habit_info/<int:habitpk>/", views.habit_info, name="habit_info"),
    path("home/habit_info/<int:habitpk>/add_log/", views.add_log, name="add_log"),
    path(
        "home/habit_info/<int:habitpk>/delete_log/<int:logpk>/",
        views.delete_log,
        name="delete_log",
    ),
    path(
        "home/habit_info/<int:habitpk>/edit_log/<int:logpk>/",
        views.edit_log,
        name="edit_log",
    ),

]