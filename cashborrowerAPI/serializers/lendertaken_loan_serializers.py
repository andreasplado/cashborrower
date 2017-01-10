from rest_framework import serializers
from ..models.models import Loan


class LenderTakenLoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields =('id','lender','borrower', 'amount','notes','loanAdded','deadline','isLoanPrivate', 'interest', 'interestInterval')
