FROM node:latest
WORKDIR /usr/src/app
EXPOSE 8080


COPY package*.json /usr/src/app/package*.json


RUN pwd



RUN ls -la /usr/src/app/


RUN npm install

CMD ["npm", "run", "build"]

