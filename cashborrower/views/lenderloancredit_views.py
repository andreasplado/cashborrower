
from ..models import Lender, LoanLike
from rest_framework.pagination import(
    PageNumberPagination
)
from rest_framework import generics
from ..serializers import lenderloancredit_serializers
from itertools import chain

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

#########################
## Lender credit views ##
#########################

class LenderLoanCreditListView(generics.ListCreateAPIView):
    serializer_class = lenderloancredit_serializers.LenderLoanCreditSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        lender = self.kwargs['lender']
        loan = self.kwargs['loan']

        lenderQuery = Lender.objects.filter(id=lender)
        loanQuery = LoanLike.objects.filter(loan=loan).order_by('-id').filter(credit=True)
        innerjoinQuery = chain(lenderQuery, loanQuery)
        return list(innerjoinQuery)

class LenderLoanDiscreditListView(generics.ListCreateAPIView):
    serializer_class = lenderloancredit_serializers.LenderLoanCreditSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        lender = self.kwargs['laender']
        loan = self.kwargs['loan']

        lenderQuery = Lender.objects.filter(id=lender)
        loanQuery = LoanLike.objects.filter(loan=loan).order_by('-id').filter(credit=False)
        innerjoinQuery = chain(lenderQuery, loanQuery)
        return list(innerjoinQuery)

class LenderLoanCreditDetailAPIView(generics.RetrieveAPIView):
    serializer_class = lenderloancredit_serializers.LenderLoanCreditSerializer
    lookup_field = 'id'
    def get_queryset(self):
        lender = self.kwargs['lender']
        loan = self.kwargs['loan']
        id = self.kwargs['id']
        lenderQuery = Lender.objects.filter(id=lender)
        loanQuery = LoanLike.objects.filter(loan=loan).filter(id=id).order_by('-id')
        innerjoinQuery = chain(lenderQuery, loanQuery)
        return list(innerjoinQuery)

class LenderLoanCreditUpdateAPIView(generics.UpdateAPIView):
    queryset = LoanLike.objects.all()
    serializer_class = lenderloancredit_serializers.LenderLoanCreditSerializer
    lookup_field = 'id'

class LenderLoanCreditDeleteAPIView(generics.DestroyAPIView):
    queryset = LoanLike.objects.all()
    serializer_class = lenderloancredit_serializers.LenderLoanCreditSerializer
    lookup_field = 'id'
    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        lender = Lender.objects.filter(id=lender_fk)
        loanCredit = LoanLike.objects.filter(loan=loan_fk).filter(id=id).order_by('-id')
        innerjoinQuery = chain(lender, loanCredit)
        return list(innerjoinQuery)