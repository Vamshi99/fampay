from background_task import background
import os

import googleapiclient.discovery
import googleapiclient.errors
from datetime import datetime, timedelta, timezone
from youtube.models import Thumbnail, Video
from django.db import IntegrityError
from django.utils import dateparse
from django.conf import settings


@background(schedule=60)
def getLatestDataFromYoutube():
    api_service_name = "youtube"
    api_version = "v3"
    custom_settings = settings.CUSTOM_SETTINGS
    KEYS_FILE = 'keys.txt'
    # Read keys from the file
    with open(KEYS_FILE) as f:
        keys = [line.rstrip() for line in f]
    print(keys)

    # Try to get data by using keys. If success, save the data to database,
    # else try to get data by using another key
    print("Getting data for search term: " + custom_settings['queryTerm'])
    for api_key in keys:
        try:
            # Get data from youtube by calling the Data v3 API using the google api client
            youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
            request = youtube.search().list(
                part="snippet",
                order="date",
                publishedAfter=(datetime.utcnow() - timedelta(seconds=custom_settings['fetchInterval'])).isoformat() + "Z",
                q=custom_settings['queryTerm'],
                type="video",
                maxResults=50
            )

            response = request.execute()
            break
        except googleapiclient.errors.HttpError as e:
            # If failed due to rate limit error, try with another key
            print(str(api_key) + " expired. Trying with another key.")
    if response is None or "items" not in response:
        print("No items in response")
        return 
    for item in response["items"]:
        try:
            print(item["snippet"]["title"])
            video = Video(
                id=item["id"]["videoId"],
                title=item["snippet"]["title"],
                description=item["snippet"]["description"],
                publishTime=dateparse.parse_datetime(item["snippet"]["publishTime"]),
                channelTitle=item["snippet"]["channelTitle"],
                channelId=item["snippet"]["channelId"],
            )
            video.save()
            for resolution,thumbnail in item["snippet"]["thumbnails"].items():
                thumbnail_obj = Thumbnail(
                    video=video,
                    url=thumbnail["url"],
                    width=thumbnail["width"],
                    height=thumbnail["height"],
                    resolution=resolution
                )
                thumbnail_obj.save()
        except IntegrityError as e:
            continue