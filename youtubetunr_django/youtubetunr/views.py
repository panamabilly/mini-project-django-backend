from .models import Youtuber
from .serializers import YoutuberSerializer
from rest_framework import generics


class YoutuberList(generics.ListCreateAPIView):
    queryset = Youtuber.objects.all()
    serializer_class = YoutuberSerializer


class YoutuberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Youtuber.objects.all()
    serializer_class = YoutuberSerializer
