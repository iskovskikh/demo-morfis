from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from .serializers import MorfisUserSerializer

# Create your views here.
from morfis_auth.models import MorfisUser
from rest_framework import views




class MorfisUserViewSet(viewsets.ModelViewSet):
# class MorfisUserViewSet(viewsets.generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MorfisUser.objects.all().order_by('-date_joined')
    serializer_class = MorfisUserSerializer
    permission_classes = [permissions.IsAuthenticated]


