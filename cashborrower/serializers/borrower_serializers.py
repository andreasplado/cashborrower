from rest_framework import serializers
from ..models import Borrower

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        #fields =('eventName')
        fields = '__all__'