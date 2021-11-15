from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics, filters

from morfis_core.morfis_models import case
from .serializers import ICDcodeSerializer


# class ICDcodeViewSet(viewsets.ModelViewSet):
class ICDcodeViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    search_fields = ['code', 'disease_description']
    filter_backends = (filters.SearchFilter,)
    queryset = case.ICDcode.objects.all()
    serializer_class = ICDcodeSerializer
    permission_classes = [permissions.AllowAny]