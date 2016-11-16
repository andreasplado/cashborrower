from ..models import User
from rest_framework.pagination import(
    PageNumberPagination
)

from rest_framework import generics
from ..serializers import user_serializers

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


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = user_serializers.UserSerializer
    lookup_field = 'id'

class UserAddAPIView(generics.GenericAPIView):
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