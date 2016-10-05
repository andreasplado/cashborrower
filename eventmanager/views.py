from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Comment, EventLike, CommentLike
from .serializers import EventSerializer, CommentSerializer, EventLikeSerializer, CommentLikeSerializer
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
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-id')
    serializer_class = EventSerializer
    pagination_class = StandardResultsSetPagination
    
    

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        key = self.kwargs['pk']
        queryset = Comment.objects.filter(event=key)
        return queryset

class EventLikeList(APIView):
    def get(self, request, *args, **kwargs):
        key = self.kwargs['pk']
        eventLikes = EventLike.objects.filter(pk=key)
        serializer = EventLikeSerializer(eventLikes, many=True)
        return Response(serializer.data)
    def post(self):
        pass


class CommentLikeList(APIView):
    def get(self, request, *args, **kwargs):
        key = self.kwargs['pk']
        commentLikes = CommentLike.objects.filter(pk=key)
        serializer = CommentLikeSerializer(commentLikes, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class GoogleCloudMessaging(APIView):
    def get(self, request, *args, **kwargs):
        #data = self.kwargs[
        #    'registration_id',
        #    'info'
        #    ]
        #gcm_send_bulk_message(data[0], data[1] )
        pass
    def post(self):
        pass