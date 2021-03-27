from core.models import Profile, Habit, HabitLog
from .serializers import ProfileSerializer, HabitSerializer, HabitLogSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics

# Create your views here.


class ProfileList(generics.ListAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class HabitList(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=profile)


# Change below to APIView with proper methods
class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitLogList(generics.ListCreateAPIView):
    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer



class HabitLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer
