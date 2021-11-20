from rest_framework.serializers import ModelSerializer,ListSerializer
from youtube.models import Thumbnail, Video

# class ListSerializer(ModelSerializer):
#     class Meta:
#         model = Video
#         fields = [
#             'id',
#             'title',
#             'text',
#         ]

class ThumbnailSerializer(ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ['url', 'width', 'height','resolution']

class VideoSerializer(ModelSerializer):
    thumbnails = ThumbnailSerializer(many=True,read_only=True)
    class Meta:
        model = Video
        fields = ('id','title','description','publishTime','channelTitle','channelId','thumbnails')