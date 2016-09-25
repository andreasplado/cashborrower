from rest_framework import serializers
from .models import Event, Comment

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        #fields =('eventName')
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        #fields =('comment')
        fields = '__all__'