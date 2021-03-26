from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("profiles/", views.ProfileList.as_view(), name="profile-list"),
    path("habits/", views.HabitList.as_view(), name="habit-list"),
    path("habits/<int:pk>/", views.HabitDetail.as_view(), name="habit-detail"),
    path("habits/<int:pk>/logs/", views.HabitLogList.as_view(), name="habit-log-list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)