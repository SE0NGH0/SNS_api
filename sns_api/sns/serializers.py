from rest_framework import serializers
from .models import Sns

class SnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sns
        fields = ('id', 'SNSemail', 'SNSpassword')