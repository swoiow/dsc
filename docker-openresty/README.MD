## openresty special

base on [Docker Hub - openresty](https://hub.docker.com/r/openresty/openresty)

  + ngx_http_substitutions_filter_module
  + Modsecurity (TODO)
  + ngx_pagespeed (TODO)

```
docker build \
--build-arg "RESTY_IMAGE_BASE=debian" \
--build-arg "RESTY_IMAGE_TAG=stable-slim" \
--build-arg "RESTY_J=4" \
--build-arg "RESTY_OPENSSL_VERSION=1.1.1b" \
--build-arg "RESTY_CONFIG_OPTIONS_MORE=--add-module=/tmp/ngx_http_substitutions_filter_module-master" \
--build-arg "RESTY_EVAL_PRE_CONFIGURE=curl -sL https://github.com/yaoweibin/ngx_http_substitutions_filter_module/archive/master.tar.gz | tar -xz" \
--build-arg "RESTY_EVAL_POST_MAKE=rm -rf /root/.cache /tmp/* /var/lib/apt/* /var/cache/* /var/log/*" \
-t openresty:slim \
-f bionic/Dockerfile . \
--no-cache
```
