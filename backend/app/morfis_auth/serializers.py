
from rest_framework import serializers

from morfis_auth.models import MorfisUser


class MorfisUserSerializer(serializers.HyperlinkedModelSerializer):
# class MorfisUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MorfisUser
        fields = ['url', 'username', 'groups','subdivision']