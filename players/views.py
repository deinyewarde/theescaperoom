from django.shortcuts import render
from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer
from django.contrib.auth.models import User

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

