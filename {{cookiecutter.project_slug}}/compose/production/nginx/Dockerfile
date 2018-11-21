FROM nginx

RUN rm -f /etc/nginx/conf.d/*
COPY compose/production/nginx/{{cookiecutter.domain_name}}.conf /etc/nginx/conf.d/default.conf