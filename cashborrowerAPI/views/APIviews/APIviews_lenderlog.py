from cashborrowerAPI.models.models import Log
from rest_framework.pagination import(
    PageNumberPagination
)
from rest_framework import generics
from cashborrowerAPI.serializers import lenderlog_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

#################
## Lender logs ##
#################
class LenderLogListView(generics.ListAPIView):
    serializer_class = lenderlog_serializers.LogSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        lender = self.kwargs['lender']
        return Log.objects.filter(lender=lender).order_by('-id')


class LenderLogDetailAPIView(generics.RetrieveAPIView):
    queryset = Log.objects.all()
    serializer_class = lenderlog_serializers.LogSerializer
    lookup_field = 'id'
    def get_queryset(self):
        lender = self.kwargs['lender']
        return Log.objects.filter(lender=lender).order_by('-id')

class LenderLogAddAPIView(generics.CreateAPIView):
    serializer_class = lenderlog_serializers.LogSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        lender = self.kwargs['lender']
        return Log.objects.filter(lender=lender).order_by('-id')


class LenderLogUpdateAPIView(generics.UpdateAPIView):
    serializer_class = lenderlog_serializers.LogSerializer
    lookup_field = 'id'
    queryset = Log.objects.all()

class LenderLogDeleteAPIView(generics.DestroyAPIView):
    serializer_class = lenderlog_serializers.LogSerializer
    lookup_field = 'id'
    queryset = Log.objects.all()