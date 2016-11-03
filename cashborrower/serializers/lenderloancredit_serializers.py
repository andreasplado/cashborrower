from rest_framework import serializers
from ..models import Lender, LoanLike

class LenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lender
        #fields =('comment')
        fields = ('email',)



class LenderLoanCreditSerializer(serializers.ModelSerializer):
    lender = LenderSerializer
    class Meta:
        model = LoanLike
        #fields =('comment')
        fields = '__all__'