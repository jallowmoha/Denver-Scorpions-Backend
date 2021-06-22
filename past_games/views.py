from .serializers import PastGamesSerializer
from .models import PastGames
from rest_framework import generics

# Create your views here.


class PastGamesList(generics.ListCreateAPIView):
    queryset = PastGames.objects.all()
    serializer_class = PastGamesSerializer


class PastGamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PastGames.objects.all()
    serializer_class = PastGamesSerializer