from rest_framework import serializers
from ..models import Log, Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('amount',)

class LogSerializer(serializers.ModelSerializer):
    loan = LoanSerializer(many=False)
    class Meta:
        model = Log
        fields =('lender', 'borrower', 'loan', 'isLoanReturned')
        #fields = '__all__'