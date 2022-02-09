from rest_framework import serializers
from .models import Youtuber


class YoutuberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtuber
        fields = ['id', 'name', 'video_title', 'video_url']
