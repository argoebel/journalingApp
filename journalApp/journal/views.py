from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from journal.serializers import UserSerializer

# Create your views here.


class UserAPIView(APIView):

    def post(self, request, format=None):
        print("YEET")
        print(request.data)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.create(serializer.validated_data)
        return Response(
            request.data,
            status=status.HTTP_200_OK
        )
