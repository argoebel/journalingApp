from rest_framework import serializers
from journal.models import User, Post


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.objects.create(**validated_data)
