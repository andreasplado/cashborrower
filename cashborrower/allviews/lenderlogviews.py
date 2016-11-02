from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Loan, LoanCredit, Comment, CommentLike, Log, LoanVote, Lender
from ..serializers import LoanSerializer, LogSerializer, LoanCreditSerializer, CommentSerializer, CommentLikeSerializer, LoanVotesSerializer, LenderSerializer
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

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

#################
## Lender logs ##
#################
class LenderLogListView(generics.ListCreateAPIView):
    serializer_class = LogSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        return Log.objects.filter(lender=lender_fk).order_by('-id')


class LenderLogDetailAPIView(generics.RetrieveAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    lookup_field = 'id'
    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        return Log.objects.filter(lender=lender_fk).order_by('-id')


class LenderLogUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LogSerializer
    lookup_field = 'id'
    queryset = Log.objects.all()

class LenderLogDeleteAPIView(generics.DestroyAPIView):
    serializer_class = LogSerializer
    lookup_field = 'log_id'
    queryset = Log.objects.all()