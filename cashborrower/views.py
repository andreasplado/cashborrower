from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Loan, LoanCredit, Comment, CommentLike, Log, LoanVote
from .serializers import LoanSerializer, LogSerializer, LoanCreditSerializer, CommentSerializer, CommentLikeSerializer, LoanVotesSerializer
from rest_framework.settings import api_settings
from rest_framework import generics
from rest_framework.pagination import(
    LimitOffsetPagination,
    PageNumberPagination
)
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework import generics, permissions
# Create your views here.
# To use pagination you must use generics

# Pagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000




##################
## Lender Loans ##
##################
class GivenLoanListView(generics.ListCreateAPIView):
    serializer_class = LoanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        lender_id = self.kwargs['lender_id']
        return Loan.objects.filter(id=lender_id).order_by('-id')

class GivenLoanListViewSearchByEmail(generics.ListCreateAPIView):
    serializer_class = LoanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        borrower_id = self.kwargs['borrower_id']
        lender_id = self.kwargs['lender_id']
        return Loan.objects.filter(lender=lender).filter(borrower=borrower).order_by('-id')


class TakenLoanListView(generics.ListCreateAPIView):
    serializer_class = LoanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        borrower_id = self.kwargs['borrower_id']
        return Loan.objects.filter(borrower=borrower_id).order_by('-id')



class LenderLoanDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LoanSerializer
    lookup_field = 'loan_id'
    
    def get_queryset(self):
        lender_id = self.kwargs['lender_id']
        return Loan.objects.filter(lender=lender_id).order_by('-id')


class LenderLoanUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LoanSerializer
    lookup_field = 'loan_id'

    def get_queryset(self):
        lender = self.kwargs['lender']
        return Loan.objects.filter(lender=lender).order_by('-id')

class PublicLoansUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LoanSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Loan.objects.order_by('-id')

class LenderLoanDeleteAPIView(generics.DestroyAPIView):
    serializer_class = LoanSerializer
    lookup_field = 'loan_id'

    def get_queryset(self):
        lender = self.kwargs['lender']
        return Loan.objects.filter(lender=lender).order_by('-id')

################
## Loan votes ##
################
class LoanVotesListView(generics.ListCreateAPIView):
    queryset = LoanVote.objects.all().order_by('-id')
    serializer_class = LoanVotesSerializer
    pagination_class = StandardResultsSetPagination


class LoanVoteUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LoanVotesSerializer
    lookup_field = 'email'

    def get_queryset(self):
        loan = self.kwargs['lender']
        return LoanVote.objects.filter(loan=loan).order_by('-id')






###################
## Loan Comments ##
###################

class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        loan_fk = self.kwargs['loan_fk']
        return Comment.objects.filter(loan=loan_fk)

class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    def get_queryset(self):
        loan_fk = self.kwargs['loan_fk']
        return Comment.objects.filter(loan=loan_fk)

class CommentUpdateAPIView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    def get_queryset(self):
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        return Comment.objects.filter(id=id).filter(loan=loan_fk)

class CommentDeleteAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    def get_queryset(self):
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        return Comment.objects.filter(id=id).filter(loan=loan_fk)

##################
## Loan Credits ##
##################

class LoanCreditListView(generics.ListCreateAPIView):
    serializer_class = LoanCreditSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):

        loan_fk = self.kwargs['loan_fk']
        return LoanCredit.objects.filter(loan=loan_fk).filter(credit=True)

class LoanDiscreditListView(generics.ListCreateAPIView):
    serializer_class = LoanCreditSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        loan_fk = self.kwargs['loan_fk']
        return LoanCredit.objects.filter(loan=loan_fk).filter(credit=False)

class LoanCreditDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    lookup_field = 'id'
    def get_queryset(self):
        loan_fk = self.kwargs['loan_fk']
        return LoanCredit.objects.filter(loan=loan_fk)

class LoanCreditUpdateAPIView(generics.UpdateAPIView):
    queryset = LoanCredit.objects.all()
    serializer_class = LoanCreditSerializer
    lookup_field = 'id'
    def get_queryset(self):
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        return LoanCredit.objects.filter(id=id).filter(loan=loan_fk)

class LoanCreditDeleteAPIView(generics.DestroyAPIView):
    queryset = LoanCredit.objects.all()
    serializer_class = LoanCreditSerializer
    lookup_field = 'id'
    def get_queryset(self):
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        return LoanCredit.objects.filter(id=id).filter(loan=loan_fk)