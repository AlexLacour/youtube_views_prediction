#!/bin/bash

docker-compose down

docker-compose up --build -d
docker exec mongodb mongoimport --db yt_db --collection projet_cs --file data.json --jsonArray

docker ps