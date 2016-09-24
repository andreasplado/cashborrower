from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer

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