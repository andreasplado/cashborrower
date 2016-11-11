
from rest_framework import serializers
from ..models import  Loan



class LenderLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields =('id','lender','borrower', 'amount','notes','deadline', 'isLoanPrivate')


class AddLenderLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('lender','borrower', 'amount','notes','deadline',
        'isLoanReturned', 'isLoanPrivate')




class LenderLoanByEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields =('lender', 'borrower','amount','notes','deadline',
        'isLoanReturned', 'isLoanPrivate')
        #fields = '__all__'
