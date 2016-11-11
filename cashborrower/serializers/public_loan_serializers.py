from rest_framework import serializers
from ..models import Loan



class LoanSerializer(serializers.ModelSerializer):
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
        fields =('id','lender', 'borrower', 'amount','notes','deadline', 'isLoanPrivate', 'loanLikeCount', 'loanDislikeCount')
        # fields = '__all__'
