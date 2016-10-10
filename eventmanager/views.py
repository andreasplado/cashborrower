from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Loan, LoanCredit, Comment, CommentLike, Log
from .serializers import LoanSerializer, LogSerializer, LoanCreditSerializer, CommentSerializer, CommentLikeSerializer
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
# Create your views here.
# To use pagination you must use generics

# Pagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

###########
## Loans ##
###########
class LoanListView(generics.ListCreateAPIView):
    queryset = Loan.objects.all().order_by('-id')
    serializer_class = LoanSerializer
    pagination_class = StandardResultsSetPagination


class LoanDetailAPIView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'id'


class LoanUpdateAPIView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'id'

class LoanDeleteAPIView(generics.DestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'id'


###########
## Logs ##
###########
class LogListView(generics.ListCreateAPIView):
    queryset = Log.objects.all().order_by('-id')
    serializer_class = LogSerializer
    pagination_class = StandardResultsSetPagination


class LogDetailAPIView(generics.RetrieveAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    lookup_field = 'id'


class LogUpdateAPIView(generics.UpdateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    lookup_field = 'id'

class LogDeleteAPIView(generics.DestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    lookup_field = 'id'



###################
## Loan Comments ##
###################

class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        loan_fk = self.kwargs['loan_fk']
        return Comment.objects.filter(loan=loan_fk)

class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    def get_queryset(self):
        loan_fk = self.kwargs['loan_fk']
        return Comment.objects.filter(loan=loan_fk)

class CommentUpdateAPIView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    def get_queryset(self):
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        return Comment.objects.filter(id=id).filter(loan=loan_fk)

class CommentDeleteAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    def get_queryset(self):
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        return Comment.objects.filter(id=id).filter(loan=loan_fk)

###################
## Loan Credits ##
###################

class LoanCreditListView(generics.ListCreateAPIView):
    serializer_class = LoanCreditSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        loan_fk = self.kwargs['loan_fk']
        return LoanCredit.objects.filter(loan=loan_fk).filter(credit=True)

class LoanDiscreditListView(generics.ListCreateAPIView):
    serializer_class = LoanCreditSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        loan_fk = self.kwargs['loan_fk']
        return LoanCredit.objects.filter(loan=loan_fk).filter(credit=False)

class LoanCreditDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    lookup_field = 'id'
    def get_queryset(self):
        loan_fk = self.kwargs['loan_fk']
        return LoanCredit.objects.filter(loan=loan_fk)

class LoanCreditUpdateAPIView(generics.UpdateAPIView):
    queryset = LoanCredit.objects.all()
    serializer_class = LoanCreditSerializer
    lookup_field = 'id'
    def get_queryset(self):
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        return LoanCredit.objects.filter(id=id).filter(loan=loan_fk)

class LoanCreditDeleteAPIView(generics.DestroyAPIView):
    queryset = LoanCredit.objects.all()
    serializer_class = LoanCreditSerializer
    lookup_field = 'id'
    def get_queryset(self):
        id = self.kwargs['id']
        loan_fk = self.kwargs['loan_fk']
        return LoanCredit.objects.filter(id=id).filter(loan=loan_fk)



'''class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination


class LoanCreditNum(APIView):
    def get(self, request, *args, **kwargs):
        key = self.kwargs['pk']
        loanCredits = LoanCredit.objects.filter(credit=True).filter(loan_id=key).count()
        return Response(loanCredits)
    def post(self, request, *args, **kwargs):
        #print(request.data)
        serializer = LoanCreditSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#downvotef for the loaner
class LoanDiscreditNum(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        key = self.kwargs['pk']
        loanCredits = LoanCredit.objects.filter(credit=False).filter(loan_id=key).count()
        return Response(loanCredits)
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = LoanCreditSerializer(data=request.data)
        if serializer.is_valid():
            key = self.kwargs['pk']
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






#comment like  must return full json because it counts all data
class CommentLikeList(APIView):
    def get(self, request, *args, **kwargs):
        key = self.kwargs['pk']
        commentLikes = CommentLike.objects.filter(pk=key).count()
        return Response(commentLikes)
    def post(self, request, *args, **kwargs):
        serializer = CommentLikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''