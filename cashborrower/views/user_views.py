from time import perf_counter

from django.contrib.auth.models import User
from rest_framework.pagination import(
    PageNumberPagination
)

from rest_framework import generics
from ..serializers import user_serializers
from rest_framework import permissions

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

#######################
## PUBLIC Loan views ##
#######################

class UserListView(generics.ListAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = user_serializers.UserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (permissions.AllowAny,)


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = user_serializers.UserSerializer
    lookup_field = 'id'
    permission_classes = (permissions.AllowAny,)


class UserByEmailDetailAPIView(generics.RetrieveAPIView):
    serializer_class = user_serializers.UserSerializer
    lookup_field = 'gmail'

    def get_queryset(self):
        gmail = self.kwargs['gmail']
        return User.objects.filter(gmail=gmail).order_by('-id')

    permission_classes = (permissions.AllowAny,)

class UserAddAPIView(generics.CreateAPIView):
    serializer_class = user_serializers.UserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (permissions.AllowAny,)

class UserExistsAPIView(generics.RetrieveAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = user_serializers.UserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (permissions.AllowAny,)

class UserAddVoteAPIView(generics.UpdateAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = user_serializers.UserSerializer
    pagination_class = StandardResultsSetPagination


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = user_serializers.UserSerializer
    lookup_field = 'id'

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = user_serializers.UserSerializer
    lookup_field = 'id'