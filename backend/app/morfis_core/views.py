import rest_framework.pagination
from django.db.models import Q

from rest_framework import permissions, generics, filters

from morfis_core.morfis_models.case import Case, IcdCode
from .serializers import ICDcodeSerializer
from .serializers import CaseSerializer
from .serializers import OrganizationSerializer
from .serializers import AddressSerializer
from morfis_auth.permissions import IsHospitalMember
from morfis_core.morfis_models.organizations import Organization
from morfis_core.morfis_models.address import Address

class MyDefaultPageNumberPagination(rest_framework.pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 10


from drf_haystack.serializers import HaystackSerializer, HighlighterMixin
from drf_haystack.viewsets import HaystackViewSet

from .search_indexes import IcdCodesIndex


class IcdCodeSearchSerializer(HighlighterMixin, HaystackSerializer):
    highlighter_css_class = "highlighted"
    highlighter_html_tag = "span"
    highlighter_max_length = 300

    class Meta:
        index_classes = [IcdCodesIndex]
        fields = [
            "text",
            "id",
            "code",
            "disease_description",
            "parent_code",
            "autocomplete",
            "highlighted"
        ]
        ignore_fields = ["autocomplete"]
        field_aliases = {
            "q": "autocomplete"
        }


class IcdCodesSearchView(HaystackViewSet):
    index_models = [IcdCode]
    serializer_class = IcdCodeSearchSerializer
    pagination_class = MyDefaultPageNumberPagination
    # pagination_class = None
    permission_classes = [permissions.AllowAny]


class IcdCodeListViewSet(generics.ListAPIView):
    queryset = IcdCode.objects.all()
    serializer_class = ICDcodeSerializer

    search_fields = ['code', 'disease_description']
    filter_backends = (filters.SearchFilter,)
    pagination_class = MyDefaultPageNumberPagination
    # pagination_class = None
    permission_classes = [permissions.AllowAny]


class IcdCodesSearchViewSet(generics.ListAPIView):
    serializer_class = ICDcodeSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            query = Q(code__icontains=search) \
                    | Q(disease_description__icontains=search) \
                    | Q(parent_code__icontains=search)
            return IcdCode.objects.filter(query)[:10]
        else:
            return IcdCode.objects.none()


class CaseCreateViewSet(generics.CreateAPIView):
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated & IsHospitalMember]

    def perform_create(self, serializer):
        serializer.save()

class CaseUpdateViewSet(generics.UpdateAPIView, generics.RetrieveAPIView):
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated & IsHospitalMember]

    def get_queryset(self):
        return Case.objects.all()


class CaseListViewSet(generics.ListAPIView):
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated & IsHospitalMember]
    search_fields = ['request_id', ]

    def get_queryset(self):
        qs = Case.objects.filter(hospital=self.request.user.hospital)
        return self.filter_queryset_for_user(qs, self.request.user)

    def filter_queryset_for_user(self, qs, user):
        return qs.order_by('add_date')

class OrganizationSearchViewSet(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated & IsHospitalMember]
    pagination_class = MyDefaultPageNumberPagination

    def get_queryset(self):
        search = self.request.query_params.get('q')
        if search:
            query = Q(title__icontains=search)
            return Organization.objects.filter(query)[:20]
        else:
            return Organization.objects.none()


class OrganizationUpdateViewSet(generics.UpdateAPIView, generics.RetrieveAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Organization.objects.all()


class OrganizationCreateViewSet(generics.CreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class OrganizationListViewSet(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = MyDefaultPageNumberPagination
    queryset = Organization.objects.all()


class AddressListViewSet(generics.ListAPIView):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = MyDefaultPageNumberPagination
    queryset = Address.objects.all()


class AddressCreateViewSet(generics.CreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class AddressUpdateViewSet(generics.UpdateAPIView, generics.RetrieveAPIView):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Address.objects.all()


class AddressSearchViewSet(generics.ListAPIView):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = MyDefaultPageNumberPagination

    def get_queryset(self):
        search = self.request.query_params.get('q')
        if search:
            query = Q(address__icontains=search)
            return Address.objects.filter(query)[:20]
        else:
            return Address.objects.none()
