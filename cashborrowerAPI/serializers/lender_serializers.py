from rest_framework import serializers
from ..models.models import Lender

class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        #fields =('eventName')
        fields = '__all__'