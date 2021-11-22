import rest_framework.pagination
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics, filters, mixins
from rest_framework.generics import GenericAPIView, get_object_or_404

from morfis_core.morfis_models import case
from .serializers import ICDcodeSerializer, CaseSerializer
from morfis_auth.permissions import IsSubdivisionMember


class MyDefaultPageNumberPagination(rest_framework.pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100


class IcdCodeListViewSet(generics.ListAPIView):

    queryset = case.IcdCode.objects.all()
    serializer_class = ICDcodeSerializer

    search_fields = ['code', 'disease_description']
    filter_backends = (filters.SearchFilter,)
    pagination_class = MyDefaultPageNumberPagination
    permission_classes = [permissions.AllowAny]



class CaseUpdateViewSet(generics.UpdateAPIView,generics.RetrieveAPIView):
    serializer_class = CaseSerializer
    queryset = case.Case.objects.all()
    permission_classes = [IsSubdivisionMember]
    # permission_classes = [permissions.IsAuthenticated]


class CaseListViewSet(generics.ListAPIView):

    # queryset = case.Case.objects.all() todo filter by subdivision
    serializer_class = CaseSerializer
    search_fields = ['request_id']
    # permission_classes = [permissions.IsAuthenticated, IsSubdivisionMember]
    # permission_classes = [permissions.OR]
    permission_classes = [IsSubdivisionMember]

    def get_queryset(self):
        qs = case.Case.objects.all().order_by('add_date')
        return self.filter_queryset_for_user(qs, self.request.user)

    def filter_queryset_for_user(self, qs, user):
        # qs = qs.filter(subdivision = user.subdivision)
        # print(qs)
        # print(user.subdivision)
        return qs

    # def get_object(self):
    #     obj = get_object_or_404(self.get_queryset())
    #     self.check_object_permissions(self.request, obj)
    #     return obj