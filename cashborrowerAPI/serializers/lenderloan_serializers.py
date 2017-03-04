
from rest_framework import serializers
from ..models.models import  Loan



class LenderLoanSerializer(serializers.ModelSerializer):
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
        fields =('id','lender','borrower', 'amount','notes','loanAdded','deadline', 'isLoanPrivate', 'interest', 'interestInterval',
                 'loanLikeCount', 'loanDislikeCount')


class AddLenderLoanSerializer(serializers.ModelSerializer):

    imageProof = serializers.ImageField(max_length=None,use_url=True)

    class Meta:
        model = Loan
        fields = ('lender','borrower', 'amount','notes','loanAdded','deadline', 'isLoanPrivate', 'interest', 'interestInterval', 'imageProof')




class LenderLoanByEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields =('lender', 'borrower','amount','notes','loanAdded','deadline',
        'isLoanReturned', 'isLoanPrivate', 'interest', 'interestInterval')
        #fields = '__all__'
