FROM ubuntu:latest

LABEL version="1.0.0"
LABEL maintainer="kishoreinvitesu@gmail.com"

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install nginx -y

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]