import rest_framework.pagination
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics, filters, mixins
from rest_framework.generics import GenericAPIView

from morfis_core.morfis_models import case
from .serializers import ICDcodeSerializer, CaseSerializer


class MyDefaultPageNumberPagination(rest_framework.pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100


class IcdCodeViewSet(generics.ListAPIView):

    queryset = case.IcdCode.objects.all()
    serializer_class = ICDcodeSerializer

    search_fields = ['code', 'disease_description']
    filter_backends = (filters.SearchFilter,)
    pagination_class = MyDefaultPageNumberPagination
    permission_classes = [permissions.AllowAny]



class CaseViewSet(generics.ListCreateAPIView):

    # queryset = case.Case.objects.all() todo filter by subdivision
    serializer_class = CaseSerializer
    search_fields = ['request_id']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = case.Case.objects.all()
        return self.filter_queryset_for_user(qs, self.request.user)

    def filter_queryset_for_user(self, qs, user):
        # qs.filter(Q(subdivision_in = user.hospital.subdivisions))
        # pass  # Your logic here
        print(user.subdivision)
        return qs