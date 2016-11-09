from rest_framework import serializers
from ..models import Loan, Lender, Borrower


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


class LoanSerializer(serializers.ModelSerializer):
    lender = LenderSerializer(many=False)
    borrower = BorrowerSerializer(many=False)
    loanLikeCount = serializers.IntegerField(
        source='loanlike_set.count',
        read_only=True
    )
    loanDislikeCount = serializers.IntegerField(
        source='loandislike_set.count',
        read_only=True
    )
    class Meta:
        model = Loan
        fields =('id','lender', 'borrower', 'amount','notes','deadline',
                 'isLoanReturned', 'isLoanPrivate', 'loanLikeCount', 'loanDislikeCount')
        # fields = '__all__'
