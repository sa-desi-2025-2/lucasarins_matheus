from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models.reparos import Reparos
from maintence.serializers.reparos import ReparosSerializer
from django.db.models import Sum, Avg, Count
from rest_framework.response import Response
from maintence.models import Usuarios
from rest_framework import serializers


class ReparosViewSet(ModelViewSet):
    queryset = Reparos.objects.all()
    serializer_class = ReparosSerializer
    permission_classes = [IsAuthenticated]

    
            