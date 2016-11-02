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

##################
## Lender views ##
##################

class LenderListView(generics.ListCreateAPIView):
    queryset = Lender.objects.all().order_by('-id')
    serializer_class = LenderSerializer
    pagination_class = StandardResultsSetPagination


class LenderDetailAPIView(generics.ListCreateAPIView):
    serializer_class = LenderSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        return Lender.objects.filter(id=id).order_by('-id')

class LenderUpdateAPIView(generics.UpdateAPIView):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer
    lookup_field = 'id'

class LenderDeleteAPIView(generics.DestroyAPIView):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer
    lookup_field = 'id'