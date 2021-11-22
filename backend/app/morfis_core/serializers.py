from rest_framework import serializers
from rest_framework.utils.representation import serializer_repr

from morfis_core.morfis_models import case


class ICDcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = case.IcdCode
        fields = ['id', 'code', ]


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = case.Case
        fields = '__all__'
        read_only_fields = (
            'created_by',
            'lastmodified_by',
        )
