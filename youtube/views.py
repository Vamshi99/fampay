from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from youtube.models import Video
from youtube.serializers import VideoSerializer
from django.db.models import Q


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

# Create your views here.
class VideoListAPIView(ListAPIView):
    serializer_class = VideoSerializer
    model = Video
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = self.model.objects.all()
        query = self.request.query_params.get('query')
        if query is not None:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return queryset.order_by('-publishTime')

# getLatestDataFromYoutube(repeat=3600)
# import asyncio
# import time

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

# async def main():
#     print(f"started at {time.strftime('%X')}")

#     task1 = asyncio.create_task(
#         getLatestDataFromYoutube(1, 'hello'))

#     # task2 = asyncio.create_task(
#     #     say_after(2, 'world'))
#     # await say_after(1, 'hello')
#     # await say_after(2, 'world')

#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())