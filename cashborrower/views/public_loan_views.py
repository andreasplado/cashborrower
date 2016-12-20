from rest_framework import permissions

from ..models import Loan, LoanLike
from rest_framework.pagination import(
    PageNumberPagination
)

from rest_framework import generics
from ..serializers import public_loan_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

#######################
## PUBLIC Loan views ##
#######################

class PublicLoanListView(generics.ListAPIView):
    queryset = Loan.objects.filter(isLoanPrivate=False).order_by('-id')
    serializer_class = public_loan_serializers.LoanSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (permissions.AllowAny,)


class PublicLoanDetailAPIView(generics.RetrieveAPIView):
    queryset = Loan.objects.filter(isLoanPrivate=False).order_by('-id')
    serializer_class = public_loan_serializers.LoanSerializer
    lookup_field = 'id'
    permission_classes = (permissions.AllowAny,)

class PublicLoanAddAPIView(generics.CreateAPIView):
    queryset = Loan.objects.filter(isLoanPrivate=False).order_by('-id')
    serializer_class = public_loan_serializers.LoanSerializer
    pagination_class = StandardResultsSetPagination


class PublicLoanUpdateAPIView(generics.UpdateAPIView):
    queryset = Loan.objects.filter(isLoanPrivate=False).order_by('-id')
    serializer_class = public_loan_serializers.LoanSerializer
    lookup_field = 'id'

class PublicLoanDeleteAPIView(generics.DestroyAPIView):
    queryset = Loan.objects.filter(isLoanPrivate=False).order_by('-id')
    serializer_class = public_loan_serializers.LoanSerializer
    lookup_field = 'id'
