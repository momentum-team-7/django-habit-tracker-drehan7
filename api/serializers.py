from rest_framework import serializers
from core.models import User, Profile, Habit, HabitLog


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
        ]


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            "id",
            "title",
            "author",
            "description",
            "goal",
        ]


class HabitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitLog
        fields = [
            "id",
            "habit",
            "date",
            "track_unit",
        ]