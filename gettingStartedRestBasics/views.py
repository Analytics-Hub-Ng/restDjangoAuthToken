from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 

from.serializers import LanguageSerializer
from .models import Language


# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]
