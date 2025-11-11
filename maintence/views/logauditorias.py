from maintence.models.logauditorias import LogAuditorias
from maintence.serializers.logauditorias import LogAuditoriasSerializer
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated


class LogAuditoriasViewSet(ModelViewSet):
    queryset = LogAuditorias.objects.all()
    serializer_class = LogAuditoriasSerializer 
