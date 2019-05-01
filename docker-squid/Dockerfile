FROM debian:stretch-slim

ARG squid_version=4.6

ENV SQUID_VERSION=$squid_version

ENV CONFIGURE="\
        --prefix=/usr/local/squid \
        "

RUN set -xe \
    && dependencies="g++ autoconf make curl ca-certificates" \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y $dependencies \

    && cd /usr/src \
    && curl http://www.squid-cache.org/Versions/v4/squid-${SQUID_VERSION}.tar.gz | tar zx \
    && cd /usr/src/squid-${SQUID_VERSION} \
    && ./configure ${CONFIGURE} \
    && make \
    && make install \

    && apt-get remove --purge --auto-remove -y $dependencies \
    && apt-get clean -y \
    && apt-get autoclean -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /usr/src/squid-${SQUID_VERSION}

STOPSIGNAL SIGTERM
