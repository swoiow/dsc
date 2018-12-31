FROM alpine:edge

ADD https://github.com/OpenGG/docker-aria2/raw/master/root/aria2.conf.default /etc/aria2.conf.default
ADD https://github.com/swoiow/dsc/raw/master/config-aria2/prepare.sh /prepare.sh

RUN set -xe \
    && apk add --no-cache \
        aria2 \
        dumb-init \

    && chmod 644 /prepare.sh \
    && chmod 644 /etc/aria2.conf.default \
    && rm -rf /var/cache/apk/*

WORKDIR /aria2

VOLUME /aria2/config /aria2/downloads

EXPOSE 6800

ENTRYPOINT ["dumb-init", "--"]

CMD ["sh", "/prepare.sh"]
