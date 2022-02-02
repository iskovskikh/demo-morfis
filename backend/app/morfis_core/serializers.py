from rest_framework import serializers
from rest_framework.utils.representation import serializer_repr

from morfis_core.morfis_models import case
from morfis_core.morfis_models import organizations
from morfis_core.morfis_models import address


class ICDcodeSerializer(serializers.ModelSerializer):
    # highlight = serializers.CharField()

    def to_representation(self, instance):
        ret = super(ICDcodeSerializer, self).to_representation(instance)

        search = self.context['request'].query_params.get('search')
        if search:
            text = '%s (%s) %s' % (instance.code, instance.disease_description, instance.parent_code)
            ret['highlighted'] = text.replace(search, '<span class="highlighted">{}</span>'.format(search))
        return ret

    class Meta:
        model = case.IcdCode
        fields = [
            'id',
            'code',
            'disease_description',
            'parent_code',
            # 'highlight'
        ]


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = case.Case
        fields = '__all__'
        read_only_fields = (
            'created_by',
            'lastmodified_by',
        )

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = organizations.Organization
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = address.Address
        fields = '__all__'
