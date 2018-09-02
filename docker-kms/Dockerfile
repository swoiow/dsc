FROM python:2-alpine
RUN apk add --no-cache --virtual curl \
    && curl -L https://github.com/swoiow/py-kms/archive/master.tar.gz | tar zx \
    && apk del curl

WORKDIR /py-kms-master
EXPOSE 1688

CMD ["python", "server.py"]
