from rest_framework import serializers
from ..models.models import Loan



class LoanSerializer(serializers.ModelSerializer):
    imageProof = serializers.ImageField(max_length=None, use_url=True)
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
        fields =('id','lender', 'borrower', 'amount','notes','loanAdded','deadline', 'isLoanPrivate', 'loanLikeCount', 'loanDislikeCount', 'interest','interestInterval', 'imageProof')
        # fields = '__all__'
