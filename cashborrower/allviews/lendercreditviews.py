from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Loan, LoanCredit, Comment, CommentLike, Log, LoanVote, Lender
from ..serializers import LoanSerializer, LogSerializer, LoanCreditSerializer, CommentSerializer, CommentLikeSerializer, LoanVotesSerializer
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
from itertools import chain

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

#########################
## Lender credit views ##
#########################

class LenderCreditListView(generics.ListCreateAPIView):
    serializer_class = LoanCreditSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        loan_fk = self.kwargs['loan_fk']

        lender = Lender.objects.filter(id=lender_fk)
        loanCredit = LoanCredit.objects.filter(loan_fk=loan_fk).order_by('-id').filter(credit=True)
        innerjoinQuery = chain(lender, loanCredit)
        return list(innerjoinQuery)

class LenderDiscreditListView(generics.ListCreateAPIView):
    serializer_class = LoanCreditSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        loan_fk = self.kwargs['loan_fk']

        lender = Lender.objects.filter(id=lender_fk)
        loanCredit = LoanCredit.objects.filter(loan_fk=loan_fk).order_by('-id').filter(credit=False)
        innerjoinQuery = chain(lender, loanCredit)
        return list(innerjoinQuery)

class LenderCreditDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LoanCreditSerializer
    lookup_field = 'id'
    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        loan_fk = self.kwargs['loan_fk']
        id = self.kwargs['id']
        lender = Lender.objects.filter(id=lender_fk)
        loanCredit = LoanCredit.objects.filter(loan_fk=loan_fk).filter(id=id).order_by('-id')
        innerjoinQuery = chain(lender, loanCredit)
        return list(innerjoinQuery)

class LenderCreditUpdateAPIView(generics.UpdateAPIView):
    queryset = LoanCredit.objects.all()
    serializer_class = LoanCreditSerializer
    lookup_field = 'id'
    queryset = LoanCredit.objects.all()

class LenderCreditDeleteAPIView(generics.DestroyAPIView):
    queryset = LoanCredit.objects.all()
    serializer_class = LoanCreditSerializer
    lookup_field = 'id'
    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        lender = Lender.objects.filter(id=lender_fk)
        loanCredit = LoanCredit.objects.filter(loan_fk=loan_fk).filter(id=id).order_by('-id')
        innerjoinQuery = chain(lender, loanCredit)
        return list(innerjoinQuery)