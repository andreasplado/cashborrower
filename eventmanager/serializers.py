from rest_framework import serializers
from .models import Loan, LoanCredit, Comment, CommentLike, Log

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        #fields =('eventName')
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        #fields =('eventName')
        fields = '__all__'

class LoanCreditSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanCredit
        #fields =('comment')
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        #fields =('comment')
        fields = '__all__'

class CommentLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentLike
        #fields =('comment')
        fields = '__all__'