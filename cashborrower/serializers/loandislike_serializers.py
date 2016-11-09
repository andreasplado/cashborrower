from rest_framework import serializers
from ..models import Loan, LoanDislike


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields =('id',)
        #fields = '__all__'

class LoanDisLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanDislike
        fields = '__all__'