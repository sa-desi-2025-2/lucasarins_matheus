from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models.alertas import Alertas
from maintence.serializers.alertas import AlertasSerializer
 
class AlertasViewSet(ModelViewSet):
    queryset = Alertas.objects.all()
    serializer_class = AlertasSerializer


