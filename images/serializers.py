from rest_framework import serializers
from .models import Images


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'background_img', 'background_alt', 'gallery_img', 'gallery_alt']