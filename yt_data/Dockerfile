FROM mongo

VOLUME ["/data/db"]
ADD data.json /data/
WORKDIR /data

CMD mongoimport --db yt_db --collection projet_cs --file data.json --jsonArray 

EXPOSE 27017
