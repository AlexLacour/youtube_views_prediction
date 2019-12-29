FROM mongo

VOLUME ["/data/db"]
ADD data.json /data/
WORKDIR /data

EXPOSE 27017

# docker build -t mongo_img .
# docker run -d -p 27017:27017 --name mongodb mongo_img
# docker exec -it mongodb bash
# # mongoimport --db yt_db --collection projet_cs --file data.json --jsonArray
# # mongo