
from cashborrowerAPI.models.models import Loan
from rest_framework.pagination import(
    PageNumberPagination
)
from rest_framework import generics
from cashborrowerAPI.serializers import lendertaken_loan_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

#############################
## Lender given loan views ##
#############################

class LenderTakenLoanListView(generics.ListAPIView):
    serializer_class = lendertaken_loan_serializers.LenderTakenLoanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        lender = self.kwargs['lender']
        return Loan.objects.filter(lender=lender).order_by('-id')