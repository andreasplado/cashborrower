from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Loan, LoanCredit, Comment, CommentLike, Log, LoanVote, Lender
from ..serializers import LoanSerializer, LogSerializer, LoanCreditSerializer, CommentSerializer, CommentLikeSerializer, LoanVotesSerializer, LoanVotesSerializer
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

#####################
## Loan votes view ##
#####################

class LoanVotesListView(generics.ListCreateAPIView):
    serializer_class = LoanVotesSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        loan_fk = self.kwargs['loan_fk']
        return LoanVote.objects.filter(loan=loan_fk).order_by('-id')


class LoanVoteDetailAPIView(generics.ListCreateAPIView):
    serializer_class = LoanVotesSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        return LoanVote.objects.filter(id=id).filter(loan=loan_fk).order_by('-id')

class LoanVoteUpdateAPIView(generics.UpdateAPIView):
    queryset = LoanVote.objects.all()
    serializer_class = LoanVotesSerializer
    lookup_field = 'id'

class LoanVoteDeleteAPIView(generics.DestroyAPIView):
    queryset = LoanVote.objects.all()
    serializer_class = LoanVotesSerializer
    lookup_field = 'id'

class LoanVoteByLenderAPIView(generics.ListCreateAPIView):
    serializer_class = LoanVotesSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        lender_id = self.kwargs['lender_id']
        loan_id = self.kwargs['loan_id']
        lender = Lender.objects.filter(id=lender_id)
        loan = Loan.objects.filter(id=loan_id).order_by('-id')
        innerjoinQuery = chain(lender, loan)
        
        return list(innerjoinQuery)