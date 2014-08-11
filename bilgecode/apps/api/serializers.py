from rest_framework import serializers

from bilgecode.apps.passage_planner.models import Passage
from django.contrib.auth.models import User


class PassageSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='user.username')
    
    class Meta:
        model = Passage
        fields = ('id', 'owner', 'user', 'date_created', 'passage_data')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'passages')