
from ..models import Loan
from rest_framework.pagination import(
    PageNumberPagination
)

from rest_framework import generics
from ..serializers import loan_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

################
## Loan views ##
################

class LoanListView(generics.ListCreateAPIView):
    queryset = Loan.objects.all().order_by('-id')
    serializer_class = loan_serializers.LoanSerializer
    pagination_class = StandardResultsSetPagination


class LoanDetailAPIView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = loan_serializers.LoanSerializer
    lookup_field = 'id'


class LoanUpdateAPIView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = loan_serializers.LoanSerializer
    lookup_field = 'id'

class LoanDeleteAPIView(generics.DestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = loan_serializers.LoanSerializer
    lookup_field = 'id'