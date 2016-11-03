
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
        lender_fk = self.kwargs['lender_fk']
        loan_fk = self.kwargs['loan_fk']

        lender = Lender.objects.filter(id=lender_fk)
        loanCredit = LoanLike.objects.filter(loan=loan_fk).order_by('-id').filter(credit=True)
        innerjoinQuery = chain(lender, loanCredit)
        return list(innerjoinQuery)

class LenderLoanDiscreditListView(generics.ListCreateAPIView):
    serializer_class = lenderloancredit_serializers.LenderLoanCreditSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        loan_fk = self.kwargs['loan_fk']

        lender = Lender.objects.filter(id=lender_fk)
        loanCredit = LoanLike.objects.filter(loan=loan_fk).order_by('-id').filter(credit=False)
        innerjoinQuery = chain(lender, loanCredit)
        return list(innerjoinQuery)

class LenderLoanCreditDetailAPIView(generics.RetrieveAPIView):
    serializer_class = lenderloancredit_serializers.LenderLoanCreditSerializer
    lookup_field = 'id'
    def get_queryset(self):
        lender_fk = self.kwargs['lender_fk']
        loan_fk = self.kwargs['loan_fk']
        id = self.kwargs['id']
        lender = Lender.objects.filter(id=lender_fk)
        loanCredit = LoanLike.objects.filter(loan=loan_fk).filter(id=id).order_by('-id')
        innerjoinQuery = chain(lender, loanCredit)
        return list(innerjoinQuery)

class LenderLoanCreditUpdateAPIView(generics.UpdateAPIView):
    queryset = LoanLike.objects.all()
    serializer_class = lenderloancredit_serializers.LenderLoanCreditSerializer
    lookup_field = 'id'
    queryset = LoanLike.objects.all()

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