
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
        #fields = '__all__'
        #field = 'email' #to make single element tuple add comma.


class LenderLoanSerializer(serializers.ModelSerializer):
    lender = LenderSerializer
    borrower = BorrowerSerializer

    class Meta:
        model = Loan
        fields =('lender','borrower', 'amount','notes','deadline',
        'isLoanReturned', 'isLoanPrivate')


class AddLenderLoanSerializer(serializers.ModelSerializer):
    lender = LenderSerializer(many=False)
    borrower = BorrowerSerializer(many=False)

    class Meta:
        model = Loan
        fields = ('lender','borrower', 'amount','notes','deadline',
        'isLoanReturned', 'isLoanPrivate')



class LenderLoanByEmailSerializer(serializers.ModelSerializer):
    lender_set = LenderSerializer(many=True, read_only=True) #use _set for backwards compability
    borrower_set = BorrowerSerializer(many=True, read_only=True)#use _set for backwards compability
    class Meta:
        model = Loan
        fields =('lender_set', 'borrower_set','amount','notes','deadline',
        'isLoanReturned', 'isLoanPrivate')
        #fields = '__all__'
