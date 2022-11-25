FROM node:latest
WORKDIR app
EXPOSE 8080


COPY package*.json ./app/


RUN ls -la

RUN ls -la ../

RUN ls -la ../app

RUN npm install

CMD ["npm", "run", "build"]

