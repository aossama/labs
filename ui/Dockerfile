# Build UI base image
FROM node:8-alpine AS frontend
WORKDIR /srv/
COPY . .
RUN npm install && npm run build

# Build UI image
FROM nginx:latest

LABEL app=ui

COPY --from=frontend /srv/dist /usr/share/nginx/html
