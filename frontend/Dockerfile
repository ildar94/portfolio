FROM node:latest
WORKDIR /app
EXPOSE 8080

ARG NODE_ENV=development
ENV NODE_ENV=${NODE_ENV}

COPY package*.json ./



COPY . .
RUN npm cache clean
RUN npm install -g npm
RUN npm install

CMD ["npm", "run", "build"]

