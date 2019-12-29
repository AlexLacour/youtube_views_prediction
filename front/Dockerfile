FROM node:8.7-alpine

RUN mkdir -p /srv/app/directory
WORKDIR /srv/app/directory

COPY package.json /srv/app/directory
COPY package-lock.json /srv/app/directory

RUN npm install 
COPY . /srv/app/directory

CMD [ "npm" , "start"]