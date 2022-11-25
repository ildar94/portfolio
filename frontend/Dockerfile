FROM node:latest
WORKDIR usr/src/app
EXPOSE 8080


COPY package*.json ./


RUN ls -la

RUN ls -la ../

RUN ls -la ../usr

RUN npm install

CMD ["npm", "run", "build"]

