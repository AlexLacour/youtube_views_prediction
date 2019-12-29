FROM mongo

VOLUME ["/data/db"]
ADD data.json /data/
WORKDIR /data

EXPOSE 27017

# CMD mongoimport --db yt_db --collection projet_cs --file data.json --jsonArray 