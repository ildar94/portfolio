FROM node:latest
WORKDIR /usr/srv/app
EXPOSE 8080


COPY package*.json /usr/srv/app/package*.json


RUN pwd

RUN ls ../../

RUN pwd

RUN ls -la /app

RUN ls -la /usr/srv/app/


RUN npm install

CMD ["npm", "run", "build"]

