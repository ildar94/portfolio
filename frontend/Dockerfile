FROM node:latest  as build
WORKDIR /app
EXPOSE 8080

ARG NODE_ENV=development
ENV NODE_ENV=${NODE_ENV}

COPY package*.json ./

RUN npm install

COPY . .


CMD ["npm", "run", "build"]

