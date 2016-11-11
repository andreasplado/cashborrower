
from rest_framework import serializers
from ..models import  Loan



class LenderLoanSerializer(serializers.ModelSerializer):
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
        fields =('id','lender','borrower', 'amount','notes','deadline', 'isLoanPrivate',
                 'loanLikeCount', 'loanDislikeCount')


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
