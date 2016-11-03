from ..models import Log
from rest_framework.pagination import(
    PageNumberPagination
)
from rest_framework import generics
from ..serializers import lenderlog_serializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 1000

#################
## Lender logs ##
#################
class LenderLogListView(generics.ListCreateAPIView):
    serializer_class = lenderlog_serializers.LogSerializer
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        lender_fk = self.kwargs['lender']
        return Log.objects.filter(lender=lender_fk).order_by('-id')


class LenderLogDetailAPIView(generics.RetrieveAPIView):
    queryset = Log.objects.all()
    serializer_class = lenderlog_serializers.LogSerializer
    lookup_field = 'id'
    def get_queryset(self):
        lender_fk = self.kwargs['lender']
        return Log.objects.filter(lender=lender_fk).order_by('-id')


class LenderLogUpdateAPIView(generics.UpdateAPIView):
    serializer_class = lenderlog_serializers.LogSerializer
    lookup_field = 'id'
    queryset = Log.objects.all()

class LenderLogDeleteAPIView(generics.DestroyAPIView):
    serializer_class = lenderlog_serializers.LogSerializer
    lookup_field = 'id'
    queryset = Log.objects.all()