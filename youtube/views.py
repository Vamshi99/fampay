from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from youtube.models import Video
from youtube.serializers import VideoSerializer
from django.db.models import Q

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

# Create your views here.
class VideoListAPIView(ListAPIView):
    serializer_class = VideoSerializer
    model = Video
    pagination_class = StandardResultsSetPagination
    # paginate_by = 100

    def get_queryset(self):
        # query = self.kwargs['query']
        queryset = self.model.objects.all()
        query = self.request.query_params.get('query')
        if query is not None:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        # return queryset
        # queryset = self.model.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return queryset.order_by('-publishTime')