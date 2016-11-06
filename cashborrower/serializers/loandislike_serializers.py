from rest_framework import serializers
from ..models import Lender, Loan, LoanLike, LoanDislike


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

class LoanDisLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanDislike
        fields = '__all__'