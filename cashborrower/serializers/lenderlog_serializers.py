from rest_framework import serializers
from ..models import Borrower, Log, Lender, Loan

class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = ('email',)

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('email',)

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('amount',)

class LogSerializer(serializers.ModelSerializer):
    lender = LenderSerializer(many=False)
    borrower = BorrowerSerializer(many=False)
    loan = LoanSerializer(many=False)
    class Meta:
        model = Log
        fields =('lender', 'borrower', 'loan')
        #fields = '__all__'