from rest_framework import serializers
from morfis_core.morfis_models import case


class ICDcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = case.IcdCode
        fields = ['id', 'code', 'disease_description', 'parent_code']


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = case.Case
        fields = '__all__'