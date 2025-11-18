from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models import Itens
from maintence.serializers.itens import ItensSerializer


class ItensViewSet(ModelViewSet):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer
