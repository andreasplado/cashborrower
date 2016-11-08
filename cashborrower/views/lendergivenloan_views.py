from django.shortcuts import render
from django.db.models import Empty
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cashborrower.models import Lender, Loan, Borrower
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
from cashborrower.serializers import lenderloan_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

#############################
## Lender given loan views ##
#############################

class LenderIsGivenLoanListView(generics.ListCreateAPIView):
    serializer_class = lenderloan_serializers.LenderLoanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        lender_fk = self.kwargs['lender']
        return Loan.objects.filter(lender=lender_fk).filter(isGivenLoan=True).order_by('-id')