FROM python:3.9.8-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /code
ADD requirements.txt /code/
ADD keys.txt /code/
RUN pip install -r requirements.txt
ADD root /var/spool/cron/crontabs/root
RUN dos2unix /var/spool/cron/crontabs/root
ADD . /code/