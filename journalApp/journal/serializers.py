from rest_framework import serializers
from journal.models import User, Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
