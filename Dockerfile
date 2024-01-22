
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3.9 python3-pip 

WORKDIR /dash

COPY . .

RUN pip3 install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:80 app:server  

# docker rmi -f $(docker images -aq)
