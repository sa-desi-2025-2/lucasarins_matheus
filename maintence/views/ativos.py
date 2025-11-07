from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models import Ativos
from maintence.serializers import AtivosSerializer

class AtivosViewSet(ModelViewSet):
    queryset = Ativos.objects.all()
    serializer_class = AtivosSerializer