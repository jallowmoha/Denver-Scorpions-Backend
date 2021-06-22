from .serializers import TableSerializer
from .models import Table
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

# Create your views here.


class TableList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['-points', '-goals_scored']



class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

