from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import authentication, permissions
from rest_framework import status
from journal.serializers import UserSerializer, PostSerializer
from journal.models import User, Post


# Create your views here.

class UserAuthAPIView(APIView):
    permission_classes = [AllowAny]

    # Logout
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(
            status=status.HTTP_200_OK
        )

    # Create User
    def post(self, request, format=None):
        print("CREATE USER")
        print(request.data)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        token = Token.objects.create(user=user)
        token_data = {"token": token.key}
        return Response(
            {**serializer.data, **token_data},
            status=status.HTTP_201_CREATED
        )


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # Get User
    def get(self, request, *args, **kwargs):
        print("GET USER")
        user = User.objects.get(pk=self.kwargs['pk'])
        serializer = UserSerializer(user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # Edit User
    def put(self, request, *args, **kwargs):
        print("EDIT USER")
        user = User.objects.get(pk=self.kwargs['pk'])
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(user, serializer.validated_data)
        return Response(
            {**serializer.data},
            status=status.HTTP_200_OK
        )

    # Delete User
    def delete(self, request, *args, **kwargs):
        print("DELETE USER")
        user = User.objects.get(pk=self.kwargs['pk'])
        user.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class PostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # Get Post
    def get(self, request, *args, **kwargs):
        print("GET POST")
        post = Post.objects.get(pk=self.kwargs['pk'])
        serializer = PostSerializer(post)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # Create Post
    def post(self, request, *args, **kwargs):
        print("CREATE POST")
        data = request.data.copy()
        data['author'] = request.user.uuid
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        print(serializer.data)
        return Response(
            {**serializer.data},
            status=status.HTTP_201_CREATED
        )

    # Edit Post
    def put(self, request, *args, **kwargs):
        print("EDIT POST")
        post = Post.objects.get(pk=self.kwargs['pk'])
        data = request.data.copy()
        data['author'] = request.user.uuid
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.update(post, serializer.validated_data)
        return Response(
            {**serializer.data},
            status=status.HTTP_200_OK
        )

    # Delete Post
    def delete(self, request, *args, **kwargs):
        print("DELETE POST")
        post = Post.objects.get(pk=self.kwargs['pk'])
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
