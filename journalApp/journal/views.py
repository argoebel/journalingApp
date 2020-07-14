from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from journal.serializers import UserSerializer
from journal.models import User, Post

# Create your views here.


class UserAPIView(APIView):

    # Create User
    def post(self, request, format=None):
        print("CREATE USER")
        print(request.data)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(
            request.data,
            status=status.HTTP_200_OK
        )

    def get(self, request, *args, **kwargs):
        print("GET USER")
        user = User.objects.get(pk=self.kwargs['pk'])
        serializer = UserSerializer(user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, *args, **kwargs):
        print("EDIT USER")
        user = User.objects.get(pk=self.kwargs['pk'])
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(user, serializer.validated_data)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request, *args, **kwargs):
        print("DELETE USER")
        user = User.objects.get(pk=self.kwargs['pk'])
        user.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
