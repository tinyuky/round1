FROM node:latest

EXPOSE 3000
EXPOSE 35729

WORKDIR /app

ADD . /app

ENV PATH /app/round1/node_modules/.bin:$PATH
RUN cd /app/round1
RUN npm install
RUN npm install react-scripts -g

