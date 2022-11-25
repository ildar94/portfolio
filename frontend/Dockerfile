FROM node:latest
WORKDIR /app
EXPOSE 8080

ARG NODE_ENV=development
ENV NODE_ENV=${NODE_ENV}

COPY package*.json ./



COPY . .

RUN npm ci

CMD ["npm", "run", "build"]

