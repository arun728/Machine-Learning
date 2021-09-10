FROM node:alpine as builder
WORKDIR '/app'
COPY package.json .
RUN npm install
COPY . .
RUN npm run build 

FROM nginx
COPY --from=builder /app/build /usr/share/nginx/html
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y vim
RUN apt-get install -y nano
