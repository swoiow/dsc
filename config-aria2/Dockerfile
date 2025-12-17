FROM alpine:3.23

ENV TZ=Asia/Shanghai \
    PUID=65534 \
    PGID=65534

WORKDIR /app

RUN set -eux; \
    apk add --no-cache \
      aria2 \
      dumb-init \
      su-exec \
      ca-certificates \
      tzdata; \
    update-ca-certificates; \
    mkdir -p /app/configs /app/downloads; \
    if [ -f "/usr/share/zoneinfo/${TZ}" ]; then \
      cp "/usr/share/zoneinfo/${TZ}" /etc/localtime; \
      echo "${TZ}" > /etc/timezone; \
    fi

# 你调过的“速度优先”配置作为默认模板
COPY --chmod=644 ./configs/aria2.conf /etc/aria2.conf
COPY --chmod=755 ./entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["dumb-init", "--"]
CMD ["/usr/local/bin/entrypoint.sh"]
