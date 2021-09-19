from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from accounts.serializers import UserRegistrationSerializer

from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.
class RegisterAPIView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            # print('user info: {}'.format(serializer.data))

            response_data =  {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutApiView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, format=None):
        try:
            refresh_token = request.data('refresh_data')  ## for getting token: token = META['HTTP_AUTHORIZATION'].split(' ')[-1]
            # print(refresh_token)
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
