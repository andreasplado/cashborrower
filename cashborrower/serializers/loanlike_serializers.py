from rest_framework import serializers
from ..models import Loan, LoanLike

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields =('id',)
        #fields = '__all__'


class LoanLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanLike
        fields = '__all__'