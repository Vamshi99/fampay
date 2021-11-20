from django.urls import path,re_path
from youtube.views import VideoListAPIView

urlpatterns = [
    path('videos/', VideoListAPIView.as_view(), name='videos'),
    # path('search/q=<', views.search, name='search'),
    re_path('videos/(?P<query>.+)/$', VideoListAPIView.as_view(), name='search'),
]
