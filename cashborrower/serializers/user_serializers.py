from rest_framework import serializers
from ..models import Loan, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        gmail= validated_data.get('gmail', None)
        if gmail is not None:
            user = User.objects.filter(gmail=gmail).first()
            if user is not None:
                return user

        user = User.objects.create(**validated_data)
        return user