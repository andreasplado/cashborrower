from rest_framework import serializers
from ..models import Lender, Loan, LoanLike

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields =('id',)
        #fields = '__all__'


class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields =('email',)
        #fields = '__all__'

class LoanLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanLike
        #fields = '__all__'