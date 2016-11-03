from django.shortcuts import render
from django.db.models import Empty
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Lender, Loan, Borrower
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
from ..serializers import lenderloan_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

#######################
## Lender loan views ##
#######################

class LenderLoansListView(generics.ListCreateAPIView):
    serializer_class = lenderloan_serializers.LenderLoanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        return Loan.objects.filter(lender=lender_fk).order_by('-id')

class LenderLoanDetailAPIView(generics.RetrieveAPIView):
    serializer_class = lenderloan_serializers.LenderLoanSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        id = self.kwargs['id']
        lender_fk = self.kwargs['lender_fk']
        return Loan.objects.filter(id=id).filter(lender=lender_fk).order_by('-id')

class LenderLoanUpdateAPIView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = lenderloan_serializers.LenderLoanSerializer
    lookup_field = 'id'

class LenderLoanDeleteAPIView(generics.DestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = lenderloan_serializers.LenderLoanSerializer
    lookup_field = 'id'

class LenderLoansListViewSearchByEmail(generics.ListCreateAPIView):
    serializer_class = lenderloan_serializers.LenderLoanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        loan_fk = self.kwargs['loan_fk']
        borrower_email = self.kwargs['borrower_email']
        
        # INNER JOIN
        lender = Lender.objects.filter(id=lender_fk).order_by('-id')
        loan = Loan.objects.filter(id=loan_fk)
        borrowerEmail = Borrower.objects.filter(email=borrower_email)
        
        innerjoinQuery = chain(lender, loan, borrowerEmail)
        if not borrowerEmail or not lender or not loan:
            return list()
        else:
            return list(innerjoinQuery)