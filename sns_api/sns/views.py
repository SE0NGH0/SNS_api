from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SnsSerializer
from .models import Sns

# Create your views here.
class SnsViewSet(viewsets.ModelViewSet):
    queryset = Sns.objects.all()
    serializer_class = SnsSerializer