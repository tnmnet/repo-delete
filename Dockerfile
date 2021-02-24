FROM node:lts-alpine
WORKDIR /usr/src/app
COPY . .
EXPOSE 8088
CMD [ "npm", "start" ]
