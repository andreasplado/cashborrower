from rest_framework import serializers
from ..models import LoanComment

class LoanCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanComment
        #fields = '__all__'
        fields = ('comment', 'commenter')
