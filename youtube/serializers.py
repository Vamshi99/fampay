from rest_framework.serializers import ModelSerializer
from youtube.models import Thumbnail, Video

class ThumbnailSerializer(ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ['resolution','url', 'width', 'height',]

class VideoSerializer(ModelSerializer):
    thumbnails = ThumbnailSerializer(many=True,read_only=True)
    class Meta:
        model = Video
        fields = ('id','title','description','publishTime','channelTitle','channelId','thumbnails')