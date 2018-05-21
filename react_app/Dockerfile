FROM node:10.1
RUN mkdir /app
WORKDIR /app
COPY package.json /app
RUN yarn install
COPY . /app
CMD yarn start