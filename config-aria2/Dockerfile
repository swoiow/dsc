# ---------- step 1: 只生成时区文件 ----------
FROM alpine:3.23 AS tz
ARG TZ=Asia/Shanghai
RUN set -eux; \
    apk add --no-cache \
      --repository=https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.23/main \
      --repository=https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.23/community \
      tzdata; \
    cp "/usr/share/zoneinfo/${TZ}" /localtime; \
    echo "${TZ}" > /timezone

# ---------- step 2: 最终运行镜像（不装 tzdata） ----------
FROM alpine:3.23

ENV TZ=Asia/Shanghai \
    PUID=65534 \
    PGID=65534

WORKDIR /app

RUN set -eux; \
    apk add --no-cache \
      --repository=https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.23/main \
      --repository=https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.23/community \
      aria2 dumb-init su-exec ca-certificates; \
    update-ca-certificates; \
    mkdir -p /app/configs /app/downloads

# 拷贝 step1 产物（这样最终镜像里没有 tzdata）
COPY --from=tz /localtime /etc/localtime
COPY --from=tz /timezone  /etc/timezone

COPY --chmod=644 configs/aria2.conf /etc/aria2.conf
COPY --chmod=755 entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["dumb-init", "--"]
CMD ["sh", "/usr/local/bin/entrypoint.sh"]
