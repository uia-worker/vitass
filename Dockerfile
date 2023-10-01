FROM alpine:3.16.0

WORKDIR /app

RUN set -xe;

COPY . .

RUN apk add --no-cache python3 py3-pip tini openrc; \
    pip install --upgrade pip setuptools-scm; \
    python3 setup.py install; \
    python3 vitass_demo/manage.py makemigrations; \
    python3 vitass_demo/manage.py migrate; \
    python3 vitass_demo/manage.py collectstatic; \
    addgroup -g 1000 appuser; \
    adduser -u 1000 -G appuser -D -h /app appuser; \
    chown -R appuser:appuser /app

USER appuser
EXPOSE 8000/tcp
ENTRYPOINT [ "tini", "--" ]
CMD [ "gunicorn", "--bind", ":8000", "--workers", "3", "--pythonpath", "/app/vitass_demo,/app/vitass_demo/app", "vitass_demo.wsgi:application"]
