FROM python:3.7-alpine

ADD worker.py /worker/

RUN echo $HTTP_PROXY
RUN echo $http_proxy
RUN unset HTTP_PROXY
RUN unset http_proxy 
RUN apk add --no-cache strace
RUN apk add --no-cache --update python3
RUN apk add --no-cache --update python3
RUN pip3 install --upgrade pip setuptools
# RUN pip3 install --upgrade pip
RUN pip3 install urllib3
# RUN pip3 install --upgrade pip setuptools
# RUN pip3 install urllib3

WORKDIR /worker/
