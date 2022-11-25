FROM node:latest
WORKDIR /app
EXPOSE 8080


COPY package*.json /app


RUN pwd

RUN ls ../

RUN pwd

RUN ls -la /app

RUN ls -la /app/


RUN npm install

CMD ["npm", "run", "build"]

