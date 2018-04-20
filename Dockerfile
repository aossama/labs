# Build backend base image
FROM python:3.5-alpine AS backend

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt && rm -rf /root/.cache

WORKDIR /srv/

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 8000

# Build service image
FROM backend

MAINTAINER Ahmed Anwar <ahmed@aossama.com>

ARG service
LABEL app=${service}

COPY ${service}/ .

CMD ["/docker-entrypoint.sh", "gunicorn"]
