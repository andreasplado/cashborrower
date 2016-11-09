from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Lender
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
from ..serializers import lender_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

##################
## Lender views ##
##################


# BASIC CRUD #
class LenderListView(generics.ListAPIView):
    queryset = Lender.objects.all().order_by('-id')
    serializer_class = lender_serializers.LenderSerializer
    pagination_class = StandardResultsSetPagination

class LenderDetailAPIView(generics.RetrieveAPIView):
    serializer_class = lender_serializers.LenderSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        return Lender.objects.filter(id=id).order_by('-id')

class LenderAddAPIView(generics.CreateAPIView):
    queryset = Lender.objects.all().order_by('-id')
    serializer_class = lender_serializers.LenderSerializer
    pagination_class = StandardResultsSetPagination


class LenderUpdateAPIView(generics.UpdateAPIView):
    queryset = Lender.objects.all()
    serializer_class = lender_serializers.LenderSerializer
    lookup_field = 'id'

class LenderDeleteAPIView(generics.DestroyAPIView):
    queryset = Lender.objects.all()
    serializer_class = lender_serializers.LenderSerializer
    lookup_field = 'id'

# SPECIAL CASES #
class LenderByEmailAPIView(generics.ListAPIView):
    serializer_class = lender_serializers.LenderSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        email = self.kwargs['lender_email']
        return Lender.objects.filter(email=email).order_by('-id')