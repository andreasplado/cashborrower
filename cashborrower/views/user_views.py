from rest_framework import viewsets

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

class UserAddAPIView(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-id')
    serializer_class = user_serializers.UserSerializer
    pagination_class = StandardResultsSetPagination
    def get_object(self):
        if self.request.method == 'PUT':
            obj, created = User.objects.get_or_create(gmail=self.kwargs.get('gmail'))
        if self.request.method == 'GET':
            obj, created = User.objects.get(gmail=self.kwargs.get('gmail'))


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = user_serializers.UserSerializer
    lookup_field = 'id'

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = user_serializers.UserSerializer
    lookup_field = 'id'