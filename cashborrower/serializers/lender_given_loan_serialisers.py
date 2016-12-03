from rest_framework import serializers
from ..models import Loan

class LenderGivenLoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields =('id','lender','borrower', 'amount','notes','deadline', 'isLoanPrivate', 'interest', 'interestInterval')
