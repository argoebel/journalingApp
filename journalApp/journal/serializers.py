from rest_framework import serializers
from journal.models import User, Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get(
            'username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = (validated_data.get('password'))
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'date', 'uuid')

    def create(self, validated_data):
        print("Serializer create method")
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
