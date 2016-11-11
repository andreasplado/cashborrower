
from rest_framework import mixins
from ..models import Loan
from rest_framework.pagination import(
    PageNumberPagination
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

class LenderLoanAddAPIView(generics.CreateAPIView):
    serializer_class = lenderloan_serializers.AddLenderLoanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        lender = self.kwargs['lender']
        return Loan.objects.filter(lender=lender).order_by('-id')

class LendersLoansList(generics.ListAPIView):
    serializer_class = lenderloan_serializers.LenderLoanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        lender = self.kwargs['lender']
        return Loan.objects.filter(lender=lender).order_by('-id')


class LenderLoanDetailAPIView(generics.RetrieveAPIView):
    serializer_class = lenderloan_serializers.LenderLoanSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        id = self.kwargs['id']
        lender_fk = self.kwargs['lender']
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
    serializer_class = lenderloan_serializers.LenderLoanByEmailSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        loan = self.kwargs['loan']

        # INNER JOIN
        loanQuery = Loan.objects.filter(email=loan)
        return loanQuery