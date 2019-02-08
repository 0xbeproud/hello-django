FROM nginx

RUN mkdir -p /app/log

COPY ./deploy/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./deploy/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf