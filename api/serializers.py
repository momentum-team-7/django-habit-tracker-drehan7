from rest_framework import serializers
from rest_framework import permissions

from core.models import User, Profile, Habit, HabitLog


class HabitSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="profile-detail"
    )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    class Meta:
        model = Habit
        fields = [
            "id",
            "title",
            "author",
            "description",
            "goal",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
        ]


class HabitLogSerializer(serializers.ModelSerializer):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    class Meta:
        model = HabitLog
        fields = [
            "id",
            "habit",
            "date",
            "track_unit",
        ]
