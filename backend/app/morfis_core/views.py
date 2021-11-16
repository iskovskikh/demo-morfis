import rest_framework.pagination
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics, filters, mixins
from rest_framework.generics import GenericAPIView

from morfis_core.morfis_models import case
from .serializers import ICDcodeSerializer


class MyDefaultPageNumberPagination(rest_framework.pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100

# class ICDcodeViewSet(viewsets.ModelViewSet):
# class ICDcodeViewSet(generics.ListCreateAPIView):
class ICDcodeViewSet(generics.ListAPIView):
# class ICDcodeViewSet(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     GenericAPIView
# ):
    """
    API endpoint that allows users to be viewed or edited.
    """

    search_fields = ['code', 'disease_description']
    filter_backends = (filters.SearchFilter,)
    queryset = case.ICDcode.objects.all()
    serializer_class = ICDcodeSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = MyDefaultPageNumberPagination
