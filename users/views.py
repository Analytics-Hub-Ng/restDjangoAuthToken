from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from .serializers import UserProfileSerializer, CustomUserSerializer

# Create your views here.
class CustomUser(APIView):
    serializer_class = CustomUserSerializer
    pass

class UserProfile(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format='json'):
        return Response(data={"hello": "world"}, status=status.HTTP_200_OK)
