from api.models import Mood
from api.serializers import MoodSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class MoodList(generics.ListCreateAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MoodDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    queryset = Mood.objects.all()
    serializer_class = MoodSerializer