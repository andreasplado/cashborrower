from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Loan
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

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

################
## Loan views ##
################

class LoanListView(generics.ListCreateAPIView):
    queryset = Loan.objects.all().order_by('-id')
    serializer_class = LoanSerializer
    pagination_class = StandardResultsSetPagination


class LoanDetailAPIView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'id'


class LoanUpdateAPIView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'id'

class LoanDeleteAPIView(generics.DestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'id'