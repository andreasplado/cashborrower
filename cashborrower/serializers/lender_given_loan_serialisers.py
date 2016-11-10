from rest_framework import serializers
from ..models import Lender, Borrower, Loan

class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = ('email',)
        #fields = '__all__'

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('email',)

class LenderGivenLoanSerializer(serializers.ModelSerializer):
    lender = LenderSerializer(many=False)
    borrower = BorrowerSerializer(many=False)

    class Meta:
        model = Loan
        fields =('id','lender','borrower', 'amount','notes','deadline',
        'isLoanReturned', 'isLoanPrivate')
