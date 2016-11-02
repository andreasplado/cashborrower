from rest_framework import serializers
from .models import Loan, LoanVote, LoanCredit, Comment, CommentLike, Log, Borrower, Lender

class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = ('email',) #to make single element tuple add comma.
        #it needs tuple to be serializable

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('email',) #to make single element tuple add comma.
        #it needs tuple to be serializable

class LoanSerializer(serializers.ModelSerializer):
    lender_fk = LenderSerializer(many=False)
    borrower_fk = BorrowerSerializer(many=False)
    class Meta:
        model = Loan
        fields =('lender_fk', 'borrower_fk', 'amount','notes','deadline','creditcount',
        'discreditcount','isUserVoted','isPrivateLoan')
        #fields = '__all__'

class LenderLoanSerializer(serializers.ModelSerializer):
    lender = LoanSerializer(many=False)
    class Meta:
        model = Loan
        fields = '__all__'


class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        #fields =('eventName')
        fields = '__all__'

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        #fields =('eventName')
        fields = '__all__'

class LoanVotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanVote
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