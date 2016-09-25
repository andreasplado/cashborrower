from rest_framework import serializers
from .models import Event, Comment, EventLike, CommentLike

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

class EventLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventLike
        #fields =('comment')
        fields = '__all__'

class CommentLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentLike
        #fields =('comment')
        fields = '__all__'