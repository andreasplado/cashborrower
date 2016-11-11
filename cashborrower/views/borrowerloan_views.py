from rest_framework import mixins
from ..models import Loan
from rest_framework.pagination import (
    PageNumberPagination
)
from rest_framework import generics, permissions
from itertools import chain
from ..serializers import lenderloan_serializers


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


#########################
## Borrower loan views ##
#########################

class BorrowerLoansList(generics.ListAPIView):
    serializer_class = lenderloan_serializers.LenderLoanSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        borrower = self.kwargs['borrower']
        return Loan.objects.filter(borrower=borrower).order_by('-id')

