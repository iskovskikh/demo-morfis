from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MorfisUserSerializer

# Create your views here.
from morfis_auth.models import MorfisUser


class MorfisUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MorfisUser.objects.all().order_by('-date_joined')
    serializer_class = MorfisUserSerializer
    permission_classes = [permissions.IsAuthenticated]