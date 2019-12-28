FROM python:3.7-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m  pip install -r requirements.txt

COPY . .

VOLUME ["/app/public"]

CMD flask run --host=0.0.0.0 --port=5000