from .serializers import ImageSerializer
from .models import Images
from rest_framework import generics

# Create your views here.


class ImageList(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer