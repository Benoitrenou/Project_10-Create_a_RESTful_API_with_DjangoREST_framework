from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    projects = serializers.HyperlinkedRelatedField(many=True, view_name='', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'first_name', 'last_name', 'email', 'projects']