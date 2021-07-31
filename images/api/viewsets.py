from rest_framework import viewsets

from images.api.serializers import ImageSerializer
from images.models import Image
from iotd.tasks import add


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        
        add.delay(20, 20)

        return super().get_queryset()
    
