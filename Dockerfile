FROM node:lts-alpine
WORKDIR /usr/src/app
COPY . .
EXPOSE 5000
CMD [ "npm", "start" ]
