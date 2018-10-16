FROM debian:9-slim

ARG DNSMASQ_VERSION=2.79-1

RUN set -ex \
    && echo "deb http://deb.debian.org/debian stable main" > /etc/apt/sources.list \
    && echo "deb http://security.debian.org/debian-security stable/updates main" >> /etc/apt/sources.list \
    && echo "deb http://deb.debian.org/debian stable-updates main" >> /etc/apt/sources.list \

    && echo "deb http://deb.debian.org/debian sid main" >> /etc/apt/sources.list \
    && printf "Package: * \nPin: release a=stable \nPin-Priority: 800" > /etc/apt/preferences \

    && apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y --no-install-recommends \
        dnsmasq=${DNSMASQ_VERSION} \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/usr/sbin/dnsmasq"]