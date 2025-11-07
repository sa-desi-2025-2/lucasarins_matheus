from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models.usuarios import Usuarios
from maintence.serializers.usuarios import UsuariosSerializer


class UsuariosViewSet(ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
