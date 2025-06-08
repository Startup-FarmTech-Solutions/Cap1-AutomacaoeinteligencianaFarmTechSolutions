from rest_framework import generics
from .models import LeituraSensor
from .serializers import LeituraSensorSerializer

class LeituraSensorListCreateView(generics.ListCreateAPIView):
    queryset = LeituraSensor.objects.all().order_by('-data', '-hora')
    serializer_class = LeituraSensorSerializer
