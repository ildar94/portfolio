FROM node:latest
WORKDIR /usr/src/app
EXPOSE 8080

RUN cd /usr/src/app

COPY package*.json .


RUN pwd



RUN ls -la /usr/src/app/

COPY /frontend .

RUN ls -la /usr/src/app/

RUN cd /usr/src/app/

RUN pwd
RUN ls -la .

RUN npm install

CMD ["npm", "run", "build"]

