FROM python:3.7-alpine

ADD app.py /scrapper/
ADD myScraper.py /scrapper/
RUN python3 -m pip install flask && python3 -m pip install bs4 && python3 -m pip install sockets
# RUN export FLASK_APP=app.py
# RUN export FLASK_ENV=development
# RUN flask run (--port 500)

WORKDIR /scrapper/
