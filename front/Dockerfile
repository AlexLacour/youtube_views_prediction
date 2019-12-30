FROM python:3.7.2-slim

EXPOSE 5002

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD python3 app.py