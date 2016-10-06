from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Loan, LoanCredit, Comment, CommentLike
from .serializers import LoanSerializer, LoanCreditSerializer, CommentSerializer, CommentLikeSerializer
from rest_framework.settings import api_settings
from rest_framework import generics
from rest_framework.pagination import(
    LimitOffsetPagination,
    PageNumberPagination
)
# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    #change the page size. (How many data models from database it loads per one page)
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000
    


# to use pagingnation you must use generics!!!!! iEg i use ListCreateAPIView
class LoanList(generics.ListCreateAPIView):
    queryset = Loan.objects.all().order_by('-id')
    serializer_class = LoanSerializer
    pagination_class = StandardResultsSetPagination
    def post(self, request, format=None):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        key = self.kwargs['pk']
        queryset = Comment.objects.filter(loan=key) #Notice thar if you change loan =key idk what happens.
        return queryset

#credit  must return full json because it counts all data
class LoanCreditList(APIView):
    def get(self, request, *args, **kwargs):
        key = self.kwargs['pk']
        loanCredits = LoanCredit.objects.filter(credit=True).filter(loanCredit=key).count()
        return Response(loanCredits)
    def post(self, request, format=None):
        serializer = LoanCreditSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#downvotef for the loaner
#credit  must return full json because it counts all data
class LoanDiscreditList(APIView):
    def get(self, request, *args, **kwargs):
        key = self.kwargs['pk']
        loanCredits = LoanCredit.objects.filter(credit=False).filter(loanCredit=key).count()
        return Response(loanCredits)
    def post(self, request, format=None):
        serializer = LoanCreditSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






#comment like  must return full json because it counts all data
class CommentLikeList(APIView):
    def get(self, request, *args, **kwargs):
        key = self.kwargs['pk']
        commentLikes = CommentLike.objects.filter(pk=key).count()
        return Response(commentLikes)
    def post(self, request, format=None):
        serializer = CommentLikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)