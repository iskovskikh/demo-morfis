
from rest_framework import serializers

from morfis_auth.models import MorfisUser


class MorfisUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MorfisUser
        fields = ['url', 'username', 'groups']