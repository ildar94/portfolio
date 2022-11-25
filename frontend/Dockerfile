FROM node:latest
WORKDIR ../usr/srv/app
EXPOSE 8080


COPY package*.json ../usr/srv/app


RUN ls -la

RUN ls -la ../

RUN ls -la ../usr

RUN ls -la ../usr/srv

RUN ls -la ../usr/srv/app



RUN npm install

CMD ["npm", "run", "build"]

