from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import LoanComment
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
from ..serializers import loancomment_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class LoanCommentListView(generics.ListCreateAPIView):
    serializer_class = loancomment_serializers.LoanCommentSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        loan = self.kwargs['loan']
        return LoanComment.objects.filter(loan=loan).order_by('-id')


class LoanCommentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = loancomment_serializers.LoanCommentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        loan = self.kwargs['loan']
        return LoanComment.objects.filter(id=id).filter(loan=loan).order_by('-id')


class LoanCommentUpdateAPIView(generics.UpdateAPIView):
    queryset = LoanComment.objects.all()
    serializer_class = loancomment_serializers.LoanCommentSerializer
    lookup_field = 'id'


class LoanCommentDeleteAPIView(generics.DestroyAPIView):
    queryset = LoanComment.objects.all()
    serializer_class = loancomment_serializers.LoanCommentSerializer
    lookup_field = 'id'