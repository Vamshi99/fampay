from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Video

# Create your views here.
# class VideoListView(ListAPIView):
#     model = Video
#     paginate_by = 100