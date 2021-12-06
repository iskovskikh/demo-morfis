import rest_framework.pagination
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics, filters, mixins
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import DjangoObjectPermissions

from morfis_core.morfis_models.case import Case, IcdCode
from .serializers import ICDcodeSerializer, CaseSerializer
from morfis_auth.permissions import IsHospitalMember


class MyDefaultPageNumberPagination(rest_framework.pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100


class IcdCodeListViewSet(generics.ListAPIView):
    queryset = IcdCode.objects.all()
    serializer_class = ICDcodeSerializer

    search_fields = ['code', 'disease_description']
    filter_backends = (filters.SearchFilter,)
    pagination_class = MyDefaultPageNumberPagination
    permission_classes = [permissions.AllowAny]


class CaseUpdateViewSet(generics.UpdateAPIView, generics.RetrieveAPIView):
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated & IsHospitalMember]

    def get_queryset(self):
        return Case.objects.all()
        # return Case.objects.filter(hospital=self.request.user.hospital)


class CaseListViewSet(generics.ListAPIView):
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated & IsHospitalMember]
    search_fields = ['request_id', ]

    def get_queryset(self):
        qs = Case.objects.filter(hospital=self.request.user.hospital)
        return self.filter_queryset_for_user(qs, self.request.user)

    def filter_queryset_for_user(self, qs, user):
        return qs.order_by('add_date')
