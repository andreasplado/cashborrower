from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Borrower
from rest_framework.settings import api_settings
from rest_framework import generics
from rest_framework.pagination import(
    LimitOffsetPagination,
    PageNumberPagination
)

from rest_framework import generics, permissions
from ..serializers import borrower_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000


####################
## Borrower Views ##
####################

class BorrowerListView(generics.ListCreateAPIView):
    queryset = Borrower.objects.all().order_by('-id')
    serializer_class = borrower_serializers.BorrowerSerializer
    pagination_class = StandardResultsSetPagination

class BorrowerAddAPIView(generics.CreateAPIView):
    queryset = Borrower.objects.all().order_by('-id')
    serializer_class = borrower_serializers.BorrowerSerializer
    pagination_class = StandardResultsSetPagination

class BorrowerDetailAPIView(generics.RetrieveAPIView):
    serializer_class = borrower_serializers.BorrowerSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        return Borrower.objects.filter(id=id).order_by('-id')

class BorrowerUpdateAPIView(generics.UpdateAPIView):
    queryset = Borrower.objects.all()
    serializer_class = borrower_serializers.BorrowerSerializer
    lookup_field = 'id'

class BorrowerDeleteAPIView(generics.DestroyAPIView):
    queryset = Borrower.objects.all()
    serializer_class = borrower_serializers.BorrowerSerializer
    lookup_field = 'id'