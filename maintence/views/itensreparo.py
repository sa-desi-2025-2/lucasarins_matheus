from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models import ItensReparo
from maintence.serializers import ItensReparoSerializer

class ItensReparoViewSet(ModelViewSet):
    queryset = ItensReparo.objects.all()
    serializer_class = ItensReparoSerializer 
