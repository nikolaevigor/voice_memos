FROM node:alpine
RUN apk add --no-cache --update build-base linux-headers
RUN mkdir /app
WORKDIR /app
COPY /react_app/* /app/
RUN yarn install
CMD yarn start