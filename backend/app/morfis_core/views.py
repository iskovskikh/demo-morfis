import rest_framework.pagination

from rest_framework import permissions, generics, filters

from morfis_core.morfis_models.case import Case, IcdCode
from .serializers import ICDcodeSerializer
from .serializers import CaseSerializer
from morfis_auth.permissions import IsHospitalMember


class MyDefaultPageNumberPagination(rest_framework.pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 10



from drf_haystack.serializers import HaystackSerializer, HighlighterMixin
from drf_haystack.viewsets import HaystackViewSet

from .search_indexes import IcdCodesIndex


class IcdCodeSearchSerializer(HighlighterMixin,HaystackSerializer):

    highlighter_css_class = "highlighted"
    highlighter_html_tag = "span"
    highlighter_max_length = 200


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
    permission_classes = [permissions.AllowAny]


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


class CaseListViewSet(generics.ListAPIView):
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated & IsHospitalMember]
    search_fields = ['request_id', ]

    def get_queryset(self):
        qs = Case.objects.filter(hospital=self.request.user.hospital)
        return self.filter_queryset_for_user(qs, self.request.user)

    def filter_queryset_for_user(self, qs, user):
        return qs.order_by('add_date')
