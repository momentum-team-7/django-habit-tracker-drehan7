from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("profiles/", views.ProfileList.as_view(), name="profile-list"),
    path("profiles/<int:pk>/", views.ProfileDetail.as_view(), name="profile-detail"),
    path("habits/", views.HabitList.as_view(), name="habit-list"),
    path("habits/<int:pk>/", views.HabitDetail.as_view(), name="habit-detail"),
    path("logs/", views.HabitLogList.as_view(), name="habit-log-list"),
    path("logs/<int:pk>/", views.HabitLogDetail.as_view(), name="habit-log-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)