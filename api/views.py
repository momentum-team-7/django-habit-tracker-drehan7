from core.models import Profile, Habit, HabitLog
from .serializers import ProfileSerializer, HabitSerializer, HabitLogSerializer

from django.http import Http404

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ProfileList(APIView):
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, format=None):
        pass

    def delete(self, request, format=None):
        pass


class HabitList(APIView):
    def get(self, request, format=None):
        habits = Habit.objects.all()
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass

    def update(self, request, format=None):
        pass

    def delete(self, request, format=None):
        pass


# Change below to APIView with proper methods
class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitLogList(generics.ListCreateAPIView):
    pass