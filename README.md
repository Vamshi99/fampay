# Fampay Assignment
A django application which shows Youtube videos data of any search term. Database will be filled with new data calling youtube API every 1 minute using a cron job. 

# Configurations
* `queryTerm` - Term to search for in Youtube search API call. BY default it is sports, to change this, Edit `queryTerm` key value in CUSTOM_SETTINGS of django settings.py 
* `fetchInterval` - To change data fetch API call interval, edit root(crontab) file in this location as needed and update `fetchInterval` value in seconds of CUSTOM_SETTINGS in django settings.py

## Design

#### Models: 

- Video - Stores user details like id, title, description, publishTime, channel ID , channel title 

- Thumbanil - Stores resolution, url, height, width. Thumbanil-Video has a ManyToOne relationship

## Environment Setup
Requirements:
- Docker
- Git

Run following commands to get the environment setup running: 
Get source code from the git repository and provide your git credentials as required
```sh
git clone https://github.com/Vamshi99/fampay.git
```

Build Docker image from Dockerfile
```sh
cd fampay/
docker-compose build
```

Start the docker container(in background) to run the django app. Django app will be running at localhost:5001 by default. Edit docker-compose.yml to change the port

Note: You can change the port number in DockerFile if needed
```sh
docker-compose up -d
```


## Endpoint details:
API Type | API Endpoint | Function |
---------| ------------ | -------- |
GET | /vidoes?query={query_term} | Get all the video details. Can take optional query parameter to fetch only videos which has given query term in video title or description. query_term should be URL encoded

Get Videos API supports pagination as well.<br/>
To get data with required page size, add a `page_size` parameter with required number to URL<br/>
and get a particular page data add `page` parameter with required page number to the URL.
Following example can be considered:<br/>
/videos?page_size=5&page=2 - This request will get data paginated with 5 records size and of page number 2.