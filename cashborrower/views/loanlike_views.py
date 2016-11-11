from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Loan, LoanLike
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
from ..serializers import loanlike_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

#####################
## Loan votes view ##
#####################

class LoanLikeListView(generics.ListAPIView):
    serializer_class = loanlike_serializers.LoanLikesSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        loan = self.kwargs['loan']
        return LoanLike.objects.filter(loan=loan).order_by('-id')


class LoanLikeDetailAPIView(generics.RetrieveAPIView):
    serializer_class = loanlike_serializers.LoanLikesSerializer
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        loan = self.kwargs['loan']
        return LoanLike.objects.filter(id=id).filter(loan=loan).order_by('-id')


class LoanLikeAddAPIView(generics.CreateAPIView):
    serializer_class = loanlike_serializers.LoanLikesSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        loan = self.kwargs['loan']
        return LoanLike.objects.filter(loan=loan).order_by('-id')


class LoanLikeUpdateAPIView(generics.UpdateAPIView):
    queryset = LoanLike.objects.all()
    serializer_class = loanlike_serializers.LoanLikesSerializer
    lookup_field = 'id'

class LoanLikeDeleteAPIView(generics.DestroyAPIView):
    queryset = LoanLike.objects.all()
    serializer_class = loanlike_serializers.LoanLikesSerializer
    lookup_field = 'id'

class LoanVoteByLenderAPIView(generics.ListCreateAPIView):
    serializer_class = loanlike_serializers.LoanLikesSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        lender_id = self.kwargs['lender_id']
        loan_id = self.kwargs['loan_id']
        loan = Loan.objects.filter(id=loan_id).order_by('-id')
        
        return loan