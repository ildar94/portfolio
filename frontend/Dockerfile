FROM node:latest
WORKDIR /app
EXPOSE 8080


COPY package*.json ../usr/srv/app


RUN pwd

RUN ls

RUN npm install

CMD ["npm", "run", "build"]

