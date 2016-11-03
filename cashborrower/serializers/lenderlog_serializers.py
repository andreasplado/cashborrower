from rest_framework import serializers
from ..models import Borrower, Log

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('email',)


class LogSerializer(serializers.ModelSerializer):
    borrower = BorrowerSerializer(many=False)
    class Meta:
        model = Log
        fields =('sum', 'isLoanLended', 'isLoanReturned', 
        'lender', 'borrower')
        #fields = '__all__'