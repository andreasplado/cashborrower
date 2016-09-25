from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Comment, EventLike, CommentLike
from .serializers import EventSerializer, CommentSerializer, EventLikeSerializer, CommentLikeSerializer

# Create your views here.

# List all events or create a new one
# events/
class EventList(APIView):
    def get(self, request):
        events =Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class CommentList(APIView):
    def get(self, request, *args, **kwargs):
        key = self.kwargs['pk']
        comments = Comment.objects.filter(pk=key)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    def post(self):
        pass

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