from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from maintence.models.reparos import Reparos
from maintence.serializers.reparos import ReparosSerializer
from django.db.models import Sum, Avg, Count
from rest_framework.response import Response

class ReparosViewSet(ModelViewSet):
    queryset = Reparos.objects.all()
    serializer_class = ReparosSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = getattr(self.request, 'user', None)
        if user and user.is_authenticated:
            serializer.save(id_usuario=user)
        else:
            serializer.save()

            